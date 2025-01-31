

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=e1cb7f952d136f64783d009f90e07adcbee5460c145f7b3dbcdafffe9a12dcde&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=b98ab6931801e83fe77ffc730f7949fb318cf6ab65c132abdd92f8e397e282c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=8567bcb735630b3a04140031fcc71a3727cd2859747ad2dd57efda3bcacdc2f0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=510d4e5ece4f47ffb3e2ee9f85bfb0f24d0ce456a0533a18ed9aa64d45fcc335&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=90bc590d1c075c8c3355498fcef88203ca4b871c40902becb31eeb9be667ef58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=fb380d8f7c4e10814cf7f28039b80b652f22266b00f19a26b0b448f90080f82e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=6a1cfb9de2f3ae246523238858ae8295895725bc55038135f826f0581c066baf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=489634930710cd5e3f41261c490d9abdfe993e6484260d39a40e263d1a9be670&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=1fbf90302f8acc4b4bfde438181ab6e3d85c51646f85199962ceeaa57453f727&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTNOMCXU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeNggyNCbvW7SKyHdEp0pqczs1C4tx831ni7muywIAFQIhALSwhAmTu%2Brr04mpJLgaedUMJWjX43JKgUTdfHyBvMbbKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyg%2B1aCOLAjWCz5V40q3AO8M1CAaQV9yRe%2BEmqx2vqsMySGfHK59ZpqBugJb3XzJTw3UOU0B13SKYEgLuTtaadc7IXk0IStF4qTo%2BfFApFwtFJ4zQILZDW3atNuLU6XaE08Rk7QuSQt8GP1vQjahFR1sW2VGe7w7h8amTM1dvZAVqtF5%2Bj1KAU0evbsqc97rfm324goEdRqb4rG1gUu4Y8XM9wtPTyWY4yBX8qtM52bYFDkmOBUA5BF5DwwzlqVXhOL4bUY1sxKiqHxb%2Fp9Nw5pl4UcwxwBKRne5SWUMRMPPQKgMz7gxuUnvmiVPyfoC%2BAGSl6xjgA2x24zc09DfKZmxp1A6o%2BFHqLhZNFDBmZTRUkpzJQ54nHEDrKxeJc7zsdTLGJvsRMwn9Ji52z%2BUq8A1%2Fh8XdwUzmajD4yFCdna16CGF3UEoYvOEX%2F%2BKI0%2BQtXj2gkfSMT%2FRgKiwnVFHyagEgbbUcH73Y4%2FXAU7520iN%2BhQ1porLrHwt6SMx2DDnSRnFzaAOXduLcQvUntApX7kTuLek7VCNbG3jmVglSJr42aI5c%2Bk6TBl45C7gsu%2BLDRmZoCE8TXQdS5qxDRZZhvivtarYEZyMCCY6NSeibQMlrcqiSGRnQ3n%2FgnX76anVUidI3XoO8eGf0dVbzDd%2FvG8BjqkAS7rtJFp3m9vhyxh8d6060omPcKHpEugPF7rLC23P6Q4bDXBuoyrlG2myngGN8x9cW9lModzPs%2FOmE0xw14gSf9e5rrYOQ4ZVQDtWidqVFfO6pDqTrFWFlBqLftEPsDmTUdQDD6ZTHwDO7ajl1yfx2tA%2F8XHsikApxSMqGjNUc5MS4%2BtOt5BCvmzz0BFxofJlDqq8DfusmfQ7fyIS%2FCKufGXFG0%2B&X-Amz-Signature=09103c526375d0400455de4f56bd85228abf81d4c0c3944e6d798992ad39a3a9&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTNOMCXU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeNggyNCbvW7SKyHdEp0pqczs1C4tx831ni7muywIAFQIhALSwhAmTu%2Brr04mpJLgaedUMJWjX43JKgUTdfHyBvMbbKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyg%2B1aCOLAjWCz5V40q3AO8M1CAaQV9yRe%2BEmqx2vqsMySGfHK59ZpqBugJb3XzJTw3UOU0B13SKYEgLuTtaadc7IXk0IStF4qTo%2BfFApFwtFJ4zQILZDW3atNuLU6XaE08Rk7QuSQt8GP1vQjahFR1sW2VGe7w7h8amTM1dvZAVqtF5%2Bj1KAU0evbsqc97rfm324goEdRqb4rG1gUu4Y8XM9wtPTyWY4yBX8qtM52bYFDkmOBUA5BF5DwwzlqVXhOL4bUY1sxKiqHxb%2Fp9Nw5pl4UcwxwBKRne5SWUMRMPPQKgMz7gxuUnvmiVPyfoC%2BAGSl6xjgA2x24zc09DfKZmxp1A6o%2BFHqLhZNFDBmZTRUkpzJQ54nHEDrKxeJc7zsdTLGJvsRMwn9Ji52z%2BUq8A1%2Fh8XdwUzmajD4yFCdna16CGF3UEoYvOEX%2F%2BKI0%2BQtXj2gkfSMT%2FRgKiwnVFHyagEgbbUcH73Y4%2FXAU7520iN%2BhQ1porLrHwt6SMx2DDnSRnFzaAOXduLcQvUntApX7kTuLek7VCNbG3jmVglSJr42aI5c%2Bk6TBl45C7gsu%2BLDRmZoCE8TXQdS5qxDRZZhvivtarYEZyMCCY6NSeibQMlrcqiSGRnQ3n%2FgnX76anVUidI3XoO8eGf0dVbzDd%2FvG8BjqkAS7rtJFp3m9vhyxh8d6060omPcKHpEugPF7rLC23P6Q4bDXBuoyrlG2myngGN8x9cW9lModzPs%2FOmE0xw14gSf9e5rrYOQ4ZVQDtWidqVFfO6pDqTrFWFlBqLftEPsDmTUdQDD6ZTHwDO7ajl1yfx2tA%2F8XHsikApxSMqGjNUc5MS4%2BtOt5BCvmzz0BFxofJlDqq8DfusmfQ7fyIS%2FCKufGXFG0%2B&X-Amz-Signature=b0f95c89417bd8dcb381f72b8c25c36f41c519d0debf821f46ad5e5d0f52c126&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTNOMCXU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeNggyNCbvW7SKyHdEp0pqczs1C4tx831ni7muywIAFQIhALSwhAmTu%2Brr04mpJLgaedUMJWjX43JKgUTdfHyBvMbbKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyg%2B1aCOLAjWCz5V40q3AO8M1CAaQV9yRe%2BEmqx2vqsMySGfHK59ZpqBugJb3XzJTw3UOU0B13SKYEgLuTtaadc7IXk0IStF4qTo%2BfFApFwtFJ4zQILZDW3atNuLU6XaE08Rk7QuSQt8GP1vQjahFR1sW2VGe7w7h8amTM1dvZAVqtF5%2Bj1KAU0evbsqc97rfm324goEdRqb4rG1gUu4Y8XM9wtPTyWY4yBX8qtM52bYFDkmOBUA5BF5DwwzlqVXhOL4bUY1sxKiqHxb%2Fp9Nw5pl4UcwxwBKRne5SWUMRMPPQKgMz7gxuUnvmiVPyfoC%2BAGSl6xjgA2x24zc09DfKZmxp1A6o%2BFHqLhZNFDBmZTRUkpzJQ54nHEDrKxeJc7zsdTLGJvsRMwn9Ji52z%2BUq8A1%2Fh8XdwUzmajD4yFCdna16CGF3UEoYvOEX%2F%2BKI0%2BQtXj2gkfSMT%2FRgKiwnVFHyagEgbbUcH73Y4%2FXAU7520iN%2BhQ1porLrHwt6SMx2DDnSRnFzaAOXduLcQvUntApX7kTuLek7VCNbG3jmVglSJr42aI5c%2Bk6TBl45C7gsu%2BLDRmZoCE8TXQdS5qxDRZZhvivtarYEZyMCCY6NSeibQMlrcqiSGRnQ3n%2FgnX76anVUidI3XoO8eGf0dVbzDd%2FvG8BjqkAS7rtJFp3m9vhyxh8d6060omPcKHpEugPF7rLC23P6Q4bDXBuoyrlG2myngGN8x9cW9lModzPs%2FOmE0xw14gSf9e5rrYOQ4ZVQDtWidqVFfO6pDqTrFWFlBqLftEPsDmTUdQDD6ZTHwDO7ajl1yfx2tA%2F8XHsikApxSMqGjNUc5MS4%2BtOt5BCvmzz0BFxofJlDqq8DfusmfQ7fyIS%2FCKufGXFG0%2B&X-Amz-Signature=0aa6d20ecdee5638b9f276339c36dd25941ab35f50648443516455602e365681&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=52c4b4debb225a43f9a4ad2d9edb7199007905a19ca02b561ed55dc7a427ab3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=a874d23079d6d03c8925cf568043bdd90277d2d222a183f29f09bdc3c636f16f&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=6af9232ce3f80bfc75fee0ca673742b42fca705fc0764642ec318ccb620536bd&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=167fa8a40ada3df20a44a21f14c574ddb4dae3be6b766250a7ab802515daebd1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=5218f61a1e1a769f8d3c759deef39f9dac5b53870e9947eb4aba3471072a32d7&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667AD2TI75%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEIGrWPmMVxeRrZMJnI1up02i3tgXsgdrmBF29mFRPXAAiEA2FwwjBP3TF3P2o5sdLB70mCPMPb5s77W6eQ2RoMuCWAqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCS%2Fgcx0NP5E6ziAKCrcA9vvxU5J3h1HguJv3gpTtmrpoEPSrxIRZdoYafe%2B76XctL55udsfZOjj7JVQoKSVhsX%2BLdUZW1YTAl7t4MTb%2BKjbTXx30QNSHQz7B4Qla1JQbnUAy8QHhBW6Pyl0AEl1F2nFAKntO4j7Y8pZy7RPQCQee%2FmuQ78x8%2FKBXRPNRlS9xBjgLvV3ctY0NzuYIjwW6Hx6tTOarmgoY9gpKFL5bQr8JPFc7LMSiOAyw14Xjgul2lQHIth08P2Z6JUBYDjIAv8chJU6PDZIZitNZ0Ewx7IgdpsMTPGUe%2F29FguZU6EsdEeFB3GKR2FmHmYmIyKB6qisJqGvDbHUy9gEauy0sXkh6ZmzRl0R55dxX8x0bRr5CKrpYbBu%2FMcXBLj6hehkIDoJYE8Vk1%2BSTbpXXW1QMJKbNzGsHcN%2BJiwmZiWpeyDWCr9xMYVU%2Bn0kGVays174kiDExQNfZc26hfP0AiLjNlpsP4W7fSjjSjbm3oZk%2BreM71cQ2U11NEOR2FsW7NrW3s4pwskgmX%2BKcSM%2F8BN4mrUx1PnMjzijC4j%2BzmG2t2z9qi9GV0LlwDIaRbc9ANvYw00cSGp%2F0huJJSi1FsiUBrTDJJ5qiDEv%2FkB9p%2FjM3%2BKO4%2FqNCvCYbyhmXujYMPv%2B8bwGOqUBcZPpz92rxncKv6co3aMlggxMBWnhbVqcR2N47Vm3H7ODGpVXeS%2BJPSnuaNxsIESYxWl1QMe0XmlMdb%2FJgtaA7rMGpFQOngRb%2BjiFPBDOuo%2FvtMKRhExKN%2BcXWH2gL2iWwalW91mBMs6q3CBfTDgm%2BuPcop6J0zmk334Uj69JfPPZBol9Yr8KhLeRDb7HmQx1rvQOsCsutcz3ZG8HA7j7C5vAsA%2BA&X-Amz-Signature=b40c3b3d422b64bd981a0572083f0b9fd641df24dfbe91aa77a9d41c1019b895&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OP2SOED%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBKbPDhZeursVVKX6WDgx8pHKrTHwWOhPrkMKJ2ksnKwIhAMbXET3sXTFyJOTG3oWLKkGUkda2PvUqwg2vRk7i9Z82KogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfDNWEckiGmHrePjYq3AM6Gh6NWB2b6%2BkB4ZhsdZsJ5BYZg8%2BTcqV7kfSkraqZd8rD9UADkfRFTSdO%2Bcu8hl%2FmSlTZwMDgCQeE2gDYnK0BVVigWtmDq8BveCg78iGNZFeT28%2BrqGwySl%2BiAKA1yfPT4mgjhfNCFJzLkbjGkT00IoOHT%2BU43BffwlZtHZ28LPWIcIscmNlgtdth3wAJoAWClQGcS7muoKGVbr8gN1ng08%2BSo8kR9g0dArrbQ1WeVYblGa3A5NJ8ZfcECnH2kItz95ZN4XtcUYT86k0J4YI0QmYmflliMy3E3S7QGGHYduReab9v2zapobSxVHIG5gAiDz3z3O2KpyF0%2FjcibyqiRPhB1YBlonUvXmS2Wb%2Fm6b%2FeCrURyq3RL9IFX9Ublijv4BDTByiemJ3b%2F9XadFopWbGeP5G5V9lFljUzfIXpzJahpwJLw%2FBVeEJjAPC9elXepi1xEv5vWZhyHixx%2BTL5meQbTMtSfkdvd40FipGineZNcwPEm7c3%2FbTu6CxmilwNxqAFg1iXRPlq3LkxM4PVMiLpI827mr8FfshADXwBioPeJgahnc%2BfWF3Q0P1jB%2BFmh5NB5EfgdHKCNtTeKmg3QXgvhVdfqxBP8KR2BG%2Bm%2BLJth0px%2BW1PiKM3ITCh%2FvG8BjqkASNOpdndjQSZfmuZZXE17UgmFu9gW0HMQthyfYYTnEVPthg0PkUAVpGOCY1QWSRdX5oK6l9yCL9V%2BuLD4Q1mzci9OEG0D9BOTC66jtSZ8V6bHWtUzS7O9FLaZzmvCiiV4T7GUBJKQKJybbNxKihfuy7tJJLaCKr1GdpKe%2FeU9X4dPla90E6Z0TkHywWELEfNTiUOdG2%2FCAFSC5SGjJncHo53gfIm&X-Amz-Signature=704f0150d53c0da80b47b7ad0c6c268a859b41e1dfee528de1d969549c173337&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OP2SOED%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBKbPDhZeursVVKX6WDgx8pHKrTHwWOhPrkMKJ2ksnKwIhAMbXET3sXTFyJOTG3oWLKkGUkda2PvUqwg2vRk7i9Z82KogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfDNWEckiGmHrePjYq3AM6Gh6NWB2b6%2BkB4ZhsdZsJ5BYZg8%2BTcqV7kfSkraqZd8rD9UADkfRFTSdO%2Bcu8hl%2FmSlTZwMDgCQeE2gDYnK0BVVigWtmDq8BveCg78iGNZFeT28%2BrqGwySl%2BiAKA1yfPT4mgjhfNCFJzLkbjGkT00IoOHT%2BU43BffwlZtHZ28LPWIcIscmNlgtdth3wAJoAWClQGcS7muoKGVbr8gN1ng08%2BSo8kR9g0dArrbQ1WeVYblGa3A5NJ8ZfcECnH2kItz95ZN4XtcUYT86k0J4YI0QmYmflliMy3E3S7QGGHYduReab9v2zapobSxVHIG5gAiDz3z3O2KpyF0%2FjcibyqiRPhB1YBlonUvXmS2Wb%2Fm6b%2FeCrURyq3RL9IFX9Ublijv4BDTByiemJ3b%2F9XadFopWbGeP5G5V9lFljUzfIXpzJahpwJLw%2FBVeEJjAPC9elXepi1xEv5vWZhyHixx%2BTL5meQbTMtSfkdvd40FipGineZNcwPEm7c3%2FbTu6CxmilwNxqAFg1iXRPlq3LkxM4PVMiLpI827mr8FfshADXwBioPeJgahnc%2BfWF3Q0P1jB%2BFmh5NB5EfgdHKCNtTeKmg3QXgvhVdfqxBP8KR2BG%2Bm%2BLJth0px%2BW1PiKM3ITCh%2FvG8BjqkASNOpdndjQSZfmuZZXE17UgmFu9gW0HMQthyfYYTnEVPthg0PkUAVpGOCY1QWSRdX5oK6l9yCL9V%2BuLD4Q1mzci9OEG0D9BOTC66jtSZ8V6bHWtUzS7O9FLaZzmvCiiV4T7GUBJKQKJybbNxKihfuy7tJJLaCKr1GdpKe%2FeU9X4dPla90E6Z0TkHywWELEfNTiUOdG2%2FCAFSC5SGjJncHo53gfIm&X-Amz-Signature=52ceec223d0a4840baca5a6b461e7f22f5f1d813def14bd58f99320478f2bac4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VGIVWQE%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpa3vJc%2BW1XgQqBUFI3QgmtsekZrnvW20mjovouPVvwAIhAP612iZl%2Fi%2BwLlBa9Fi1CtWxsFFNrq0vXp2RHyf94gUjKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcXsfFFqr6MrgMP70q3ANyuC2E9ulR7SXB4BB8BUxhABVLDs3uA2nttW3PC6ZsjAEo4uodaTFmbMRW3Y8PJwLl%2F94ik8NL%2BSAPXkE%2Bas4mAjxTwQUeNg0beOPFrWVuDvXqfH0N5CK2r5ymEr7cXwyuHUulX4KYnO%2BNFypimuBoMfq3ASMmRN%2BtapKaiSs24NBcXLTf0fbUbiAvD%2FG09ZaKwP96e5lISJ90APv%2FMWEt9l1G9d1kkrzrNCT3Ckl60YNLLWRfN0%2BsjnzBh8tEUeFPzuXZVawOaNSSRxrkoRQ27w1tuABSjhsiXKGk3k%2FCE10VxVPrBB298HCF2gIs825mqQdoyhAdfTaq6hcBSDiA95yTC%2BhV0BVGaTc7dRd%2B%2BLwZQo1U%2BoRnMUzLPIG6yreEl3voSSPsPlmet7eaoPsaKZsEN1XTFUUUikT03IOpjsirYucISN5bB%2B1AxZrXtwtwO9sm7x56sAFTXueriPioy9gHOZSXuz1%2FjDBiOpqxBMUYIEN3OCZ01YHZfDxnrLYzhuOuQgt9%2FpUo3N2S46pC9zEvyoHKmibTD5xBgKUGO4kRWpDo%2BocewI7BZ3KA4ezE1LPCJIPxOt1m1qdrpsNKSqFWJb%2FODmQOYk%2B2fgwDAq418Oo%2B822Z%2ByS0VzCC%2FvG8BjqkAWuLZftEd%2Fn2tfm2Zsb%2BbK%2FtNBmCSkayrl6U1Mc7wz6X39IK7o5rZF%2BmfqqinIa0KFPAHffeAEcYonwalHzwdxJUIsgn0YVmRt7QQGQwn%2FuhUM1jPh6vaYURV0CKi709LAMNlmUB9v5JRKLLQvJPbUUK61TKTEBgil%2BgYtqm7wMMajSXP2aHKZbJb8POMdxAtAq3B9EJc13lncqoPhZVZie%2Fgj%2F8&X-Amz-Signature=b93b438333706fe5da357c6e89b6c0dbdbd127c7994e97e035e60b78fe635fe0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMYSWVYA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T081842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC1GxUiWoaqgbrTUylCePXfRxwLpEZTeGwIGx7ri7hb2AiB6QW72ei62LxmgA73gdSt6KYQL%2FyRbJnuLBxi38%2F%2F94yqIBAi5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjyeeguzjE47plI42KtwDsxP%2BlTFkOeb4DobEZgCEF1CZ6Hb8iMDgZP2Ey0MN9sVy3ITHp55%2Bc51%2FXEtm%2Fau%2B7LDA3wnsEAAIh5CuzabUlnDyITYqulu0P0NPEujD1qUxXViBCuz8gwY90EVzt10lPyuVyu05I%2BrJuG%2BATzJoRTEphz3PZ6BdWm9XafkOyT9I4dpwyNbsAqT45h8%2FsCsegiwS2NTxxDiKFGu1yOvds33KxgVJ2YQrE3lAH%2Fr3buUB6Mw2O%2FQYjvOgJIG%2FFlWx9fpA3kUqhcqUj3s7UqO4AWi1MNsaKNjtUOi4G9ST7V%2FLuBx5SCd9dSSdJ7QV7yhXbQrpgOAjypN60GhNgvinrQFFL%2BlCPY7fgagrLYtEZYHyv%2FobLjBULejOu8nAngCK5TLuNBdXSY%2FSUmHMvHkSjWbraujAW23dB0bCct9RSzvE3FoeUFnTtRR7dy2ZQ%2FcanlffMfw0FRlbdWGrBLvkdL1U9d20U1UamP6f3lVvJ%2Bm3CMoFVXWXt3o3zcD4kg3zh9hd96wMnqzzHDRKGrnTuFDZrDVDmVs8iGubBo%2FPnlUds4d6Ce3kT7hqsAWiXq8gugRD9bNjGfNd7zbOt1cev%2BGg425a009tnq7AKbO7x8SYXmtd5uuHskWHxwgw7P3xvAY6pgF%2BzWp1T%2FX%2Fr3dQBzkYdt750r%2F1VXcuTpQyr34Bmvc%2B4%2BMAeAqo59MKEBpRXPpxeKbIJylcKJcApK0lmPiBeeZmFGpk5749jVUQ2P33UVfmTfEipS%2FcesgJTiKvw6LenC17xOrrVG%2B2IKBe8agSNtdQFbrip2%2BOcF0eSCOUSQi%2FD%2BZtQMLzuQZDF03Xaa%2FWDSKGNQx13unCjGE7zISSjD6LNoYgtkTg&X-Amz-Signature=90010834e560bae1a596fa96eb31e875bb932b64de7b5f444380e4f73f621d45&X-Amz-SignedHeaders=host&x-id=GetObject)
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