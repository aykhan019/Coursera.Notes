

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=cf40a99ba85a48737cf94de5593f3e872088b338506bd6464b8929058a1a238b&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=ece1c722dc9f2494f21cf4e5e4fafeaa018b2c3382f1f8fb3c0b78f50552e58d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=c14202c5d76b4bb440062ff47c024b16102d3c3c54ad5050c8511981ff8fc020&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=8cf5bf1142dfdf6071df4779aac0bf131130676b2f18dc7c5c3c456ea985c2f6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=20657072cd52dfad6d7c01a8921947ec7467b62817b9129dfac15011c70c84b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=f644e3c2b859de6e846f9546a3ab377ba04aad3df2f05565bc5800d67d7a151c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=238639090052c2b65091a5f076c2358390f99a966228248416368ee65e49edc7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=4c3ecfad0f5436699cf670a96b2a9e6e15cfe477c23b4f8e1582acd67664ba62&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=f282d0aa6df600343d8822772aeecfa18398a6a3c1bc20fe0cf0fba58a261b9e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WECMERH4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIDJzVjCkc5TjEI14lXqewFZKzKvw7nyQ4%2Fti8Uy7zRZfAiEAjPFphyoeiDirb1aSRqO1rDUAfmoZdRcGWHjHZXhsy1Qq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOXIUdXhMfh%2BY0yxFSrcA7O4GgXi4U05F0RYyVX1efwHbkC1sIoZYRVbR1dhR%2Ba32EIzICGUfHBfF%2BqL20DZ2fJNbYUSL2A%2BR0tgM7s%2FqgXp%2BTwFVbGCdaQMN8Kv92RdfsjB4ofbA4aQ9phlReZPD1NguC29ZZWC13NRnU1wLbhz42tVM%2BfUCKPGO7BtJVSzQpI5ZUigc6swKEbZ4wOvdZH9iaiKrEjX2yGQKgdMpXYHdo8L9x%2FQbyKA2DUdEXjg77Vg6Y29EK4OkKZNeY6p%2BxHzv5zCP%2BGcRNjcvDdMjwqkuNj5Al9fZriQclQ4p3mwXHz3WIROeXxZxqrGxprahLFbsecmr8Bk8CDUkxxHv0BikjRAAEePF7%2FFo2GVpikOp7qvU8bXIS9aDfsUO0VtNTrCFLTiOvJc7cmF28PwmQhfrE%2FEMd6p4BbgR6o%2F2s2%2Fr7eu%2FAqbLIOsncJG%2F4wEhcLVG1NjaUp%2F7DpMZvMxcXPEUOkY5M%2Fqo%2Bf4jyYpvjr7ZzIExMI6DfoME5LD4%2B4P2pMWYzz5g0V8Ish7e4XlpUr5vG8oRRRLz392Nx6WcUatOpfdc8FIdfvDWv481ekYJkFuZHi6iNq1ZComvJ0rHBnrItU%2FLC%2BKnXY57s1sdFZJWrJVIWhLMWEV83p1MPv%2Bmb0GOqUB72RCetVGWuRY%2FIWTFpr9cw7QG892AM%2FNdqBZ8gtbfhQ0FOyvPawT2nM%2BK1Uj9gYT2SSnrNsp6M4Au7DDCKeT%2Fzd6jtAkPDLcZVuanBriyawfMSTwxJ1AdDidzVjLCdZbhVWlQCMQ%2BK9eksEBOKEGaq55TTX9Ej6OrPDfo1CsZK%2FhbRWaEg4qoCrWS4XYPM131eSmbXXls7UadXxeKc9E%2FTkKRJi8&X-Amz-Signature=122e65d7840a2eb9a78d4242d41434ae9e677385fc95ea5861d9b85886d5e61e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WECMERH4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIDJzVjCkc5TjEI14lXqewFZKzKvw7nyQ4%2Fti8Uy7zRZfAiEAjPFphyoeiDirb1aSRqO1rDUAfmoZdRcGWHjHZXhsy1Qq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOXIUdXhMfh%2BY0yxFSrcA7O4GgXi4U05F0RYyVX1efwHbkC1sIoZYRVbR1dhR%2Ba32EIzICGUfHBfF%2BqL20DZ2fJNbYUSL2A%2BR0tgM7s%2FqgXp%2BTwFVbGCdaQMN8Kv92RdfsjB4ofbA4aQ9phlReZPD1NguC29ZZWC13NRnU1wLbhz42tVM%2BfUCKPGO7BtJVSzQpI5ZUigc6swKEbZ4wOvdZH9iaiKrEjX2yGQKgdMpXYHdo8L9x%2FQbyKA2DUdEXjg77Vg6Y29EK4OkKZNeY6p%2BxHzv5zCP%2BGcRNjcvDdMjwqkuNj5Al9fZriQclQ4p3mwXHz3WIROeXxZxqrGxprahLFbsecmr8Bk8CDUkxxHv0BikjRAAEePF7%2FFo2GVpikOp7qvU8bXIS9aDfsUO0VtNTrCFLTiOvJc7cmF28PwmQhfrE%2FEMd6p4BbgR6o%2F2s2%2Fr7eu%2FAqbLIOsncJG%2F4wEhcLVG1NjaUp%2F7DpMZvMxcXPEUOkY5M%2Fqo%2Bf4jyYpvjr7ZzIExMI6DfoME5LD4%2B4P2pMWYzz5g0V8Ish7e4XlpUr5vG8oRRRLz392Nx6WcUatOpfdc8FIdfvDWv481ekYJkFuZHi6iNq1ZComvJ0rHBnrItU%2FLC%2BKnXY57s1sdFZJWrJVIWhLMWEV83p1MPv%2Bmb0GOqUB72RCetVGWuRY%2FIWTFpr9cw7QG892AM%2FNdqBZ8gtbfhQ0FOyvPawT2nM%2BK1Uj9gYT2SSnrNsp6M4Au7DDCKeT%2Fzd6jtAkPDLcZVuanBriyawfMSTwxJ1AdDidzVjLCdZbhVWlQCMQ%2BK9eksEBOKEGaq55TTX9Ej6OrPDfo1CsZK%2FhbRWaEg4qoCrWS4XYPM131eSmbXXls7UadXxeKc9E%2FTkKRJi8&X-Amz-Signature=fdf74029a2b2914a2b7eaba0c9d6b7094aab488b15099059d10b0b469995034c&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WECMERH4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIDJzVjCkc5TjEI14lXqewFZKzKvw7nyQ4%2Fti8Uy7zRZfAiEAjPFphyoeiDirb1aSRqO1rDUAfmoZdRcGWHjHZXhsy1Qq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOXIUdXhMfh%2BY0yxFSrcA7O4GgXi4U05F0RYyVX1efwHbkC1sIoZYRVbR1dhR%2Ba32EIzICGUfHBfF%2BqL20DZ2fJNbYUSL2A%2BR0tgM7s%2FqgXp%2BTwFVbGCdaQMN8Kv92RdfsjB4ofbA4aQ9phlReZPD1NguC29ZZWC13NRnU1wLbhz42tVM%2BfUCKPGO7BtJVSzQpI5ZUigc6swKEbZ4wOvdZH9iaiKrEjX2yGQKgdMpXYHdo8L9x%2FQbyKA2DUdEXjg77Vg6Y29EK4OkKZNeY6p%2BxHzv5zCP%2BGcRNjcvDdMjwqkuNj5Al9fZriQclQ4p3mwXHz3WIROeXxZxqrGxprahLFbsecmr8Bk8CDUkxxHv0BikjRAAEePF7%2FFo2GVpikOp7qvU8bXIS9aDfsUO0VtNTrCFLTiOvJc7cmF28PwmQhfrE%2FEMd6p4BbgR6o%2F2s2%2Fr7eu%2FAqbLIOsncJG%2F4wEhcLVG1NjaUp%2F7DpMZvMxcXPEUOkY5M%2Fqo%2Bf4jyYpvjr7ZzIExMI6DfoME5LD4%2B4P2pMWYzz5g0V8Ish7e4XlpUr5vG8oRRRLz392Nx6WcUatOpfdc8FIdfvDWv481ekYJkFuZHi6iNq1ZComvJ0rHBnrItU%2FLC%2BKnXY57s1sdFZJWrJVIWhLMWEV83p1MPv%2Bmb0GOqUB72RCetVGWuRY%2FIWTFpr9cw7QG892AM%2FNdqBZ8gtbfhQ0FOyvPawT2nM%2BK1Uj9gYT2SSnrNsp6M4Au7DDCKeT%2Fzd6jtAkPDLcZVuanBriyawfMSTwxJ1AdDidzVjLCdZbhVWlQCMQ%2BK9eksEBOKEGaq55TTX9Ej6OrPDfo1CsZK%2FhbRWaEg4qoCrWS4XYPM131eSmbXXls7UadXxeKc9E%2FTkKRJi8&X-Amz-Signature=8c036ac00f2f6762d0d709527306eb5336182ed9d8d244fae2e97577c3ac4e53&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=819545b74fbb6744b4dc03fc23228ea3abbbfba805a4c929fdfd06ff2c5f301b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=91b3fa36e1b3019acc3f8ec1e165e7ede5fc13281dbe2edc6a46efd67cf834eb&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=39427e9689974d9d70af1d8c76ee3642dc3a9b7310302671927615c560e1bb62&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=b85542907c77db1b7942e16a9d9e168dd0228a2b2cf676d33219bc1dadb8de20&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=1c2ddc9cec59f813e6b107b04a9a539c7e7896e4a7f7ae79fcb98d4843001052&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHCGR3WS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIGlLDPtwm%2FLG%2BGfkA3RGt03ZIpymwt4BnLfCwhzkHlB1AiBo%2Bo1%2Fs4UG67eon5NG5h7LlLj%2FGgGzt4JrHvL%2FKz0vlCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMoA8aKUmMYRGj%2FSAGKtwDOaqQV0RakSiaVyoYieZfYZSwxmhy1lZ1f6d6fD2vZmjLAsbFvJG7rOeTnchoqiOJTf477o3OB7RwWiOJKzieR4GhYEryHjb3%2Fpn1aPS2568H%2FnWqwnL4GNtcbx0ReA3%2BExiqyTAXu9693NK9D4SKuTOZpMxVxOxTaW%2B%2Fyz%2BAIbZbZf%2B4e585mY84yrkoMxwmc829S6S3uhWi3%2B5R%2FS%2BfmrW7o8AY9y8%2F12DuubOyruBh9J7zRqD6Fc1SgptbLUa12g8DIGEvwGBvWt0ztMSORA9K2OgZgLzFsQ1%2FDpuPoijDg1YyALR4Pi3c5X7Oo2TtibnRdBWhzb9%2FnVMpNQoogtjTGAldul2jOvaWDeSHmIhjGXmohxXpnrIeDw9DAJpIzZRsWNqwqkOtpEKeLV2kHrJbrAaiPkbGXSlU%2Bf5A%2FboIoCFyfIfIRlQ66O2wLLHags2FZksFivxB32mzqPIYQztWRyrLMCoxSz7Yb%2BwRpKpMv3qLFXUML6L5%2BRuuoTryw6Ihhx9RXKZtlFYqb6htf7%2F6Hd8NUGtZB1B42BtWthS2EVdyrDjW2IbSGTc4Q466gpBASFjd6qu9qomk9C4nxQRVuR0tcq%2FM7ShFVI8bkQkwER%2FN%2Bs%2B9ai3Bticwtf6ZvQY6pgEJej%2BK8d8wY8AH99GO6Wtzn%2FiT3ecY4akY1%2FILndtGKtSAPK4Y11B5y9iV9IzwySi1L4m%2F9hdHOsF%2BoQySvrbIGi4FFYtrojCPRlslAMLXyX7ImXVHS7Y4G0Skd5Bz4Xo7WEKBW1JpF9uPtG6r0UltZq%2B1MtqyAPdwcd3xZWwVVqo5BpukfTiZSORnfyS8TmYz6iIzKnLGoAaquN0g4AfQpIadWWGx&X-Amz-Signature=32adbc3e4311e772672cb1fc25d7281108fca53bd85492c81c43e38662c3135e&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RSD4Z7B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQC4OgxUE3LWJ%2BUf8087KNKBwbqJr9ZKuPgQ0%2FiZPlxwkgIgL7GiRvI8sctC3gmcEEYxazYwArERnzJvtiUXEgp6HBEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDCsG3188NhrixYs3VyrcA5SZW0SUpfkgs7iRG93zZtNht%2FKP0ZSMGLu7ysyBMwE1JtiZpH6g239psMfrcp30Ku1lXsyV1NZfhGe9WTHwrWd6R9MRd%2Fb%2BF6C00ll2%2Fsuie0IyxXp8HxrdvyTXOJggKclTfRueiflFxRa2TGrGBTXovQCKAaXCL%2BSO7wlUpsYr6Uzf6nL9UFbKka5x%2FrCsXlBSdKcmqoiAApQVAt61ufho9Gy9gQtl0KzPzJwTzoHfcgpr7ETUV63EO%2BOXnKvlvYT3euZXo7X4pdc8cFiVRurcDDAwd3gcZw7ot4hQwWT8Irr1fPYOrKXTugHTxk5CL%2FVtELYEarILeGTktupNdQ2TIHNbMifGIriQ9ZPZ03IvprFzxJhHOKyZ%2BF%2BLMfpiSqp7RNXvTBkOnOUMW1ssF2MEoTsVIkhsprbnNnArwihN9zfuyLs%2Bdp%2Fn4oJRTGoH0NEUnYfVSBWtE4LgYrtFC5jazuw6p55IcQ%2BG4glR8oBYUai8NbtXUUEJmxOZhsBBCsiIWZx2VYUgyQo4A04kSL6LyyvdVHG%2FdxdwzscPpnWGG%2BdPHmzW25tlSevkkJsiYRz%2BdKtNjop8R4HIxyKb3CpSkdO4oJ50uWj28Y7wZb7fLBKpATSFGm%2BuarDqMJf%2Bmb0GOqUBp%2FsB8E4DJdBC%2Ffv3IOIVglFVeKQWgCYeS2rzO9L0nU2XW5nvOyPVNI1DQAbgi4vV3LGeXsI04ISSgzdNLQ2kYFA0yM4YuajsISK%2BkvDqwcN2aKZpxZ7G4egvrz60qbD3TZ8xj%2FkAADVCxjoQUwxsKaEr0LQUaIC8lY7hK1iWMQ8OvOzpwUSEFPUe0ow1I5g9NIhWLAnyBcD7EAzycZrDxSXXauTw&X-Amz-Signature=1e28114bfa503d2570c16051603654afc9a1ee944c2846f6ad42c07d09fd953a&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RSD4Z7B%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIQC4OgxUE3LWJ%2BUf8087KNKBwbqJr9ZKuPgQ0%2FiZPlxwkgIgL7GiRvI8sctC3gmcEEYxazYwArERnzJvtiUXEgp6HBEq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDCsG3188NhrixYs3VyrcA5SZW0SUpfkgs7iRG93zZtNht%2FKP0ZSMGLu7ysyBMwE1JtiZpH6g239psMfrcp30Ku1lXsyV1NZfhGe9WTHwrWd6R9MRd%2Fb%2BF6C00ll2%2Fsuie0IyxXp8HxrdvyTXOJggKclTfRueiflFxRa2TGrGBTXovQCKAaXCL%2BSO7wlUpsYr6Uzf6nL9UFbKka5x%2FrCsXlBSdKcmqoiAApQVAt61ufho9Gy9gQtl0KzPzJwTzoHfcgpr7ETUV63EO%2BOXnKvlvYT3euZXo7X4pdc8cFiVRurcDDAwd3gcZw7ot4hQwWT8Irr1fPYOrKXTugHTxk5CL%2FVtELYEarILeGTktupNdQ2TIHNbMifGIriQ9ZPZ03IvprFzxJhHOKyZ%2BF%2BLMfpiSqp7RNXvTBkOnOUMW1ssF2MEoTsVIkhsprbnNnArwihN9zfuyLs%2Bdp%2Fn4oJRTGoH0NEUnYfVSBWtE4LgYrtFC5jazuw6p55IcQ%2BG4glR8oBYUai8NbtXUUEJmxOZhsBBCsiIWZx2VYUgyQo4A04kSL6LyyvdVHG%2FdxdwzscPpnWGG%2BdPHmzW25tlSevkkJsiYRz%2BdKtNjop8R4HIxyKb3CpSkdO4oJ50uWj28Y7wZb7fLBKpATSFGm%2BuarDqMJf%2Bmb0GOqUBp%2FsB8E4DJdBC%2Ffv3IOIVglFVeKQWgCYeS2rzO9L0nU2XW5nvOyPVNI1DQAbgi4vV3LGeXsI04ISSgzdNLQ2kYFA0yM4YuajsISK%2BkvDqwcN2aKZpxZ7G4egvrz60qbD3TZ8xj%2FkAADVCxjoQUwxsKaEr0LQUaIC8lY7hK1iWMQ8OvOzpwUSEFPUe0ow1I5g9NIhWLAnyBcD7EAzycZrDxSXXauTw&X-Amz-Signature=45e6823df29a13a0950cd42a401eb74fa12d793807955279efb5b7def5f447b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DUZMVAY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCIB8Sc5mDlJURpbjWKExZW9OsbPqCB%2Bvjg%2Fw9fQYkyWjkAiEA9A9HzNtX9J3ftZyKtDG3c1UrA23O28QZfe%2Fey2ahFzcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDMuqapaTZ4B9BpXkkyrcA6Kb7sZW1zFFkBPM1M2hwOWubDg8z5en9%2FcPVfugYuOgg3pW%2FXbd8OyXTowc8jdCKUs%2BkegJJd%2BwKwDof%2Bz0fOdcQYUMEn5iw8izQxFawDLZ6tTwIqsYcCnrUbJ%2B3Ri%2F9tW6A%2BEDwxW2%2F8pQpSWy27s8fIyltsPwEDsp4lteRjK%2FEgdtz1F0HehFUYGPb5p0wvgWKLzX%2BaCy%2B0NwLIBWvMHLlZQJu44eyHgcmry%2BcPChybXjVQHsDPmLx%2BSZnh7vnOcr1uYjK%2FE2LNCXizWJyRxqpoDlDYIFxuICBJtfrBe12XjbHOzLI9I3V4b8gCNuGPmgC4sKwHu5gciFBQdW9AqoSsV81mehhmOcg8R7TM%2F5mYO7h6rWct7oI%2BFDI9afxENCbmr6AZh8G3Ie0afIIk%2FUo6Jhl9KkRoNtySc5I8brhNE4lAGr8D5YSUaCVSRiO24oUgUq2JE7OUcxwaJK0%2ButACGqnJPQkG7vrHomNQ6NNgUNAwfKx2oQRWYS%2FnZ8lmKHJ%2FQpshguhtIocEQj%2B7yw%2FFqVMvSM4NPiYQSLuIiERvfL03NWZGWx9Z3xK1PZbNOm0Eqsf9AlG8r6N91UNj06790euiccS4dblMOBc%2BZr5fCATtGIzHh%2By6WRMJ7%2Bmb0GOqUBsgQEbG9%2FK%2BbA6NTFCwVzV%2Bh30UFcqj8hXsr5DYUx6nw82N6Ak1mNrqfqz99jO7GeWcf9qCIUOqQdDAXO%2BQ3fTZnXZAxpi7Z0gDaUWMHVOcBHYAdBo6KiQSwX7gd554PUOW7%2BYyTEdFqa1WtZoMeagMY3lpe59p%2Bu3ataM7WyHR3Z6043nDptYZvPWdWo2EGNFPTk392cvHeHS6%2FPnzoQyNWYuUXP&X-Amz-Signature=6767513501baee7a2b4889c67b7097e705f7b304de3218949d48471338b29742&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672DQOQXS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDFIfh0%2FG8MC%2Fv16ms6mldgypmTLycF3o%2FEToLieXEdeAiBwK%2FRMXWkPUqyKB%2FCzw195MbUBao6uVG%2FXBCQTNk1U%2Fyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMzch3QrOeNX7qZ82SKtwDfs4u1Mf7QuG4JTA8URXGCo%2Bu%2Fa8sPbLaV%2BNZRn9xqTFUa2e9kH30v1bxueZ5D0t4c0YoWxuaZYcdjI0fiHBS76N4Yg7PxMo%2FlvU7fmB8%2Fj6eYqXG6p%2Fo3DRfDbQmZN5d8Wz1hgElH6IEASdqwX%2BnM2BHOPosHFOX1COQIOFn468p%2FY%2F6J6otzD45mwDpH3Ioh%2FoLit8aucwpMzjoZlD4X5S%2Fz8v894mEL1cqxi%2BkioHFO7ayl4GkwD4vHXfWH8rDM8cSsSM39%2B84qvROIeklxGHeDlkzbedkBmlJt70MkrI242PkXa493whcS6aujOb2zJo4LNtKar9SNU5QEXC1VD8KR04KbCrpz%2F2DkGM2D22dj35TVDeeDVRfbe1rFLYKyCbpvM8HFn1BiyHNDHzV%2BXZktHBkCNENeb9jh2ZUMzXpuEmwQfCOvfeL8fQ3WLJKvSQlqsHvo73oWShaITLlparUBBXkTaD7Fi2XzMR0BkI6bmcDBkvA9AbMTNmIMHiY4ZBt3%2BJg7kGI357i5pRdEFJ00ZaPFk2aXRvHmS0k2E%2B11DUdyuua4EulHbOMDm9kYPVwq%2B%2FDb2AZk%2BEBgfJLcNVr8Z11xTUN0fCaAlwdpyQr%2BjseYijBY4ZgkWwwhv%2BZvQY6pgHoT7n27cNjm30tZRLW4O1v33UG5HkvxgrSGAPNEZyT1BRKWRsjEZlPXLF0Ty9qJuZPcbsR8Tuu%2BmcwaF2hBCY2TQiMZbDVn8BcLdHpPgMMO%2F8MvlBTytfzycjLSMVF4C3l9WGd9OXqOIqEABSyY3N5p83uGrRewJwgbjxd0PXHDsAh8IRuAIsguFypPGVEGBj98tv74SrnmI6Wyq9NZ1IIJMoZ4iY2&X-Amz-Signature=6f080af8c005aa37be38106a2ba69c80b84936ea6a096407ab006151001894cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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