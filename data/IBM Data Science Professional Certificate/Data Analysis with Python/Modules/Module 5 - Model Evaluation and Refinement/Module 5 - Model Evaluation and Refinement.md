

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=8f1ae8f4f6653fc5200ed2596da2adebe3d84b44759522aad959f5fee75b7f29&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=381ea8888ac75d44f3cb9e7c86468fd1e64488e8747cd7346a727a6e6f50e274&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=3515636a5cca31b593a8428802b71997533bafc888fa93def1b330daf2152dd4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=e486769303b7ad7249ec8643e47034dc54f6b692c38bea01c4bf04a83da3e853&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=132351c212e0b95c11ef8cc796e10ed9f86d7d6e5f9164da3984ad525b3d1648&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=a02994d92480f69d1c7f517c7bf269a069b3741386b2a01decc9d4d82e4561c4&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=eaba4298358dc91ea20ec8a821a695f816e85c240cc7029f259d044e06a2e811&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=fd5bd0895d4f84de89ecbbe9a199600f849d071da4b4afb39660e6014275c5e2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=369a28fc41e810809501662a2e6cb6e8276cb84f769ca44a653b33b4eaf75641&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIIGPC7Z%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB4wxfnsaSMXWlyskEFyPSvKh9hS%2FLj72ZnCZz0A1WFHAiBZGHpqaJVzc0IpIOI91OtHyRS83TPs1QyjZ5QrnKMwhyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMzAuwBLBDxy83JuTBKtwDjvsbp0GVVcKnyr%2F9ofbPPoy3b3ayjTJugwnP9YxMY8e26cpgR7Ji%2BQlDNDPSII0HSpS6Z%2BNMCZZaEMSXU%2FkYMqVGim0uTvzvbHj9ogjjiSQYp0YruFOjgQ3OxRUSM1npqFjFlLy1EwAERdv5pwXoVz4leGOTUPqIoILwHM7E8UbVIFN%2FJTPXiulIhpEk9EVV0L5QtbmgxfPtpzayd8i25dJiSik4XpAJvmzt%2F519R8zaxBDa5GtMg%2BhqdZpSKtBbfy6FZSEoUhgwKF%2BeII%2BatcCWbL4K2%2F410M8etkwfWMmlV4tP8M1uswytArhv84LFx9RVFrqJQKdUnmPl06A1Hpx%2B9eB18809N4auFTnSaNHIWN4smuGijhXVyw4IOqmxy%2BKCjWx25SwLhrwJmwk2dSeUNmEbOyQEvTmFTP1etzqQ16nr2bER6BzCa1xfdYeHN7hOAx4sPJUeZO4Vd6CG%2F%2Bbri9SBEBRRi%2ByzkTesvvmJ3ZR3JBfAlIye7Ah2rEQEId1O5%2FO4x9MOSAsnirV0hf%2FTIaD%2B6uVIDxSIsKvL0PfeMTOvNwSnRA53pWh028lVwKZlyGBNQGJdFZ8yLkcTKOzyBHFZqAQ5dT7vYirYElB9rsAQddIWcePvFSEwvL6GvQY6pgEla6OVf50FjMdyF%2BVdulEkJV0lYkhgUJYf1qUVNM5hmns3NHYJuXTPW%2F42wsKBiLLhkP0tcQVRj6yNNE%2B%2B1BJ7BDijIDdbtARb%2BgHn0%2BiLasDcRjXk8CObb1%2FjltsaNLj04n4vT%2BLucaFnPZ2DONUz94KSpL809dU7r9j4qYwEXIkAjOniXfY5FI%2BIdPcNeiAyKP2Osvw8bXG7cf1BmhaTQDIGkgbt&X-Amz-Signature=bd7d53c8ff96a714e482be52a215e28d48b7ed8090041d15e7b9c505cf2df375&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIIGPC7Z%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB4wxfnsaSMXWlyskEFyPSvKh9hS%2FLj72ZnCZz0A1WFHAiBZGHpqaJVzc0IpIOI91OtHyRS83TPs1QyjZ5QrnKMwhyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMzAuwBLBDxy83JuTBKtwDjvsbp0GVVcKnyr%2F9ofbPPoy3b3ayjTJugwnP9YxMY8e26cpgR7Ji%2BQlDNDPSII0HSpS6Z%2BNMCZZaEMSXU%2FkYMqVGim0uTvzvbHj9ogjjiSQYp0YruFOjgQ3OxRUSM1npqFjFlLy1EwAERdv5pwXoVz4leGOTUPqIoILwHM7E8UbVIFN%2FJTPXiulIhpEk9EVV0L5QtbmgxfPtpzayd8i25dJiSik4XpAJvmzt%2F519R8zaxBDa5GtMg%2BhqdZpSKtBbfy6FZSEoUhgwKF%2BeII%2BatcCWbL4K2%2F410M8etkwfWMmlV4tP8M1uswytArhv84LFx9RVFrqJQKdUnmPl06A1Hpx%2B9eB18809N4auFTnSaNHIWN4smuGijhXVyw4IOqmxy%2BKCjWx25SwLhrwJmwk2dSeUNmEbOyQEvTmFTP1etzqQ16nr2bER6BzCa1xfdYeHN7hOAx4sPJUeZO4Vd6CG%2F%2Bbri9SBEBRRi%2ByzkTesvvmJ3ZR3JBfAlIye7Ah2rEQEId1O5%2FO4x9MOSAsnirV0hf%2FTIaD%2B6uVIDxSIsKvL0PfeMTOvNwSnRA53pWh028lVwKZlyGBNQGJdFZ8yLkcTKOzyBHFZqAQ5dT7vYirYElB9rsAQddIWcePvFSEwvL6GvQY6pgEla6OVf50FjMdyF%2BVdulEkJV0lYkhgUJYf1qUVNM5hmns3NHYJuXTPW%2F42wsKBiLLhkP0tcQVRj6yNNE%2B%2B1BJ7BDijIDdbtARb%2BgHn0%2BiLasDcRjXk8CObb1%2FjltsaNLj04n4vT%2BLucaFnPZ2DONUz94KSpL809dU7r9j4qYwEXIkAjOniXfY5FI%2BIdPcNeiAyKP2Osvw8bXG7cf1BmhaTQDIGkgbt&X-Amz-Signature=21d627ccf81be0238b55cb490e8dc9aa895095d7bc8ee0120ca81803f9a4d27e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIIGPC7Z%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB4wxfnsaSMXWlyskEFyPSvKh9hS%2FLj72ZnCZz0A1WFHAiBZGHpqaJVzc0IpIOI91OtHyRS83TPs1QyjZ5QrnKMwhyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMzAuwBLBDxy83JuTBKtwDjvsbp0GVVcKnyr%2F9ofbPPoy3b3ayjTJugwnP9YxMY8e26cpgR7Ji%2BQlDNDPSII0HSpS6Z%2BNMCZZaEMSXU%2FkYMqVGim0uTvzvbHj9ogjjiSQYp0YruFOjgQ3OxRUSM1npqFjFlLy1EwAERdv5pwXoVz4leGOTUPqIoILwHM7E8UbVIFN%2FJTPXiulIhpEk9EVV0L5QtbmgxfPtpzayd8i25dJiSik4XpAJvmzt%2F519R8zaxBDa5GtMg%2BhqdZpSKtBbfy6FZSEoUhgwKF%2BeII%2BatcCWbL4K2%2F410M8etkwfWMmlV4tP8M1uswytArhv84LFx9RVFrqJQKdUnmPl06A1Hpx%2B9eB18809N4auFTnSaNHIWN4smuGijhXVyw4IOqmxy%2BKCjWx25SwLhrwJmwk2dSeUNmEbOyQEvTmFTP1etzqQ16nr2bER6BzCa1xfdYeHN7hOAx4sPJUeZO4Vd6CG%2F%2Bbri9SBEBRRi%2ByzkTesvvmJ3ZR3JBfAlIye7Ah2rEQEId1O5%2FO4x9MOSAsnirV0hf%2FTIaD%2B6uVIDxSIsKvL0PfeMTOvNwSnRA53pWh028lVwKZlyGBNQGJdFZ8yLkcTKOzyBHFZqAQ5dT7vYirYElB9rsAQddIWcePvFSEwvL6GvQY6pgEla6OVf50FjMdyF%2BVdulEkJV0lYkhgUJYf1qUVNM5hmns3NHYJuXTPW%2F42wsKBiLLhkP0tcQVRj6yNNE%2B%2B1BJ7BDijIDdbtARb%2BgHn0%2BiLasDcRjXk8CObb1%2FjltsaNLj04n4vT%2BLucaFnPZ2DONUz94KSpL809dU7r9j4qYwEXIkAjOniXfY5FI%2BIdPcNeiAyKP2Osvw8bXG7cf1BmhaTQDIGkgbt&X-Amz-Signature=c347a5f9241d8a72de7c34d04f58aa95727fa73e53566f393a88c5de8a04402e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=c1a6f40ac4213f79cbe7904138a1fa97082b0e78ab62743a032ebe0b28e9a514&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=21bf30b2c6072a62bd7e43482e4aa1741a4d630aff6fb6af9f886c1fef31b296&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=9275da85221c23be213ada24a4fde3dd202d357be2394de1276e7d3a92f95494&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=a4d2170bfd89f750766220ae759dedaa795d7282c86af55dc313341db56fb61b&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=32a8279b11f51133c0609a894ceef24311213f6247de9dcc7e07a28e25c56319&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6K7QZ2U%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQDZSg%2Fy%2Fw4JGn3HAPqfA%2Btc7gTwhgERnC68zja6bvD8mgIgHNdBNtYhjuQEVGDVqg3Iuet7Q5rULWQOTUnZK0EoTPcq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDDL6unbYsmSPjMDsSSrcAzJFA%2FaXJq2lkrzGgoekTs3bQmam7zf6ze9WMVHco%2FIM172ZSnz2pFfXE7Ldp4J4WiUB%2BTXDnEBvLFp3L9t2s6ionD9uiT1993hgB6DuwQGkuAnBNVizD3QSqbEf3rH9DqWjMtoWgYY5QJ7DQfYtzD8JTTVU80GbG0Z0lyuPp1J2%2FbxKN%2B0HPSby3e2gJvVLzJCJn6ubjpg89DEQ7ycVkf3V9b3sDYVGHGNJuBrvmU%2B%2F1nHsMEg63QvLk8991TQmpMH22F4TxfCS9ZfHzWdLCcD7YMNoX24L2EfHG8tdeJ90%2B%2B3AmFRtThRqsmrXaG0vi9YpTVMeEWj46BkUl1LtS4H3JSlvgYq7%2FgTUrPrUI0kNnUuORgddTtz9S5SPMOX79GRgh%2FY3DU5A1xEw3v%2FQqIdxjDZXZDvwup9sz3G2b3ljwItLkTvuAMzycqDbvHHe4prIn3UjR6K3euOcKl3lGwjDkhGqMVqoB08bPIyBJLYhnWGxFc3UQ0o%2F7HQvWjO608eZ0wzalR2ftTjePmrVzP16wX%2BYMvPcxorl96EuKNu8gzIUm1OKkoJIt1sTX1E6GdQo9JaMPq6O4HQptkgcekA8c9SHPi9h9uoo38BBCnxBuAVpCkh6JBzPvN8OMIS%2Fhr0GOqUBzpm1UYAZvO7CD4nLzEWrZXFs5DG504nw3p9y6ct1rPjhqUbxr%2FekGgsRQ2SqpoSi94L4PLV4NT5QxJHyVkUW%2F4kzh%2BogpAvicTw%2Fe4RJm1aERJLs%2FvXy2sDXRZKB66OjOvG4Bm0v9brdXbyIKo%2BQORk6HkVFjaGfIH7lOk94OUbBtk072buGmhS%2BwHlQ9lWb0%2Btp13lB6cgAaigyHbJSiAdzFYuK&X-Amz-Signature=ff89653a72200793ae3112f663a8b1c7f786c459e7feb44d895d21bd0e57ea15&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VNPVB46%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCjRyYFnWXWcDqAR4Nkvg7DdqLRLU%2FkG07ehUgNc5I0RQIhALQoAsCNiKknWzxYZ1XdKe7N%2FA45UT6HBzi%2FX%2FAzXcvDKv8DCCYQABoMNjM3NDIzMTgzODA1IgxAMd4dmW%2BFswi0%2BZMq3ANhkNDQmhNtvF09PeXaldxt23dKcEg21DkxyL4doEe8r%2Fd4WlGyv8TUEEpGh0TKCB%2FG73bPgGibgLU229kFA9Wkw6YV0Om4UuGKw0Y9V0fjlfqHjWj4m6Q4rf0Evq%2F8V8qs99tJhwRohOlH5EaBEISkNSAJ48tkB%2Brd4IzOX2reK9Ftpc%2F5PWEymZ2TQkrjmOUXJRx%2FB0qfMhsIdbgzBhqoTsRZtIjeVoQUbneCL3BhhOd8YXlM1mQqU2L%2B%2Bxmcmfd5Z5S0zImt2Lmq6tBIDhB6vuwezf4TZPlthtt4n4C%2FiL0XF8t56JvX%2FvWzE4osTk9s1RprB5eeNjCzh%2FX3Nyh7O9WOfD7K7uZNAPFlemxdlmNdfj6W4Rhch953uTo3VCOSz%2FJveklgeA2SkgtWCDOeVU9vFG1SfA6Q7ILwWTRc4ygQy6vnNFJCEUzNgUwwh%2BwUDeU5P7julzznpU3XJXi3amdZVdzdo2%2FUhD%2F1F3nwQbJzjcMaWTfxIyyeqYMmHptVIsejgh%2BEdNcfCpQHJ2W5fNg4Cf%2FCpCQQzDGljfHTZ2kw7yhy1G05bI92Tn1CZuycRekc8SXe%2BOQPmlVNLjm6GNwqJLNehnhcbaNo4ABj7xGfqtFroq%2BFS847bTDmvoa9BjqkAadtWATA5%2F5OAHkYRvhvWsXkCrEaf5lfRTHRF9UcsmPn8BPokU8041wDC26DZHGImfRMXN6G%2BQrYfYbPK6w1UtqAs5q7HRFC7WFjLy6K7Sgh6kyjjL0LZBcJPMJstxQ5EhLnUvt6QsK5JmKGjkSWV9q4cdU9nNvLulun2Zj3ud22%2Bb6NYqHFP8fNANbq0edOQYVj6OMhimmYBm1FT9kplf4Z1s8I&X-Amz-Signature=a7227e49f8b9d91463f767b1a3f9602e7d93f73c0480430db4052034aacfd780&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VNPVB46%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCjRyYFnWXWcDqAR4Nkvg7DdqLRLU%2FkG07ehUgNc5I0RQIhALQoAsCNiKknWzxYZ1XdKe7N%2FA45UT6HBzi%2FX%2FAzXcvDKv8DCCYQABoMNjM3NDIzMTgzODA1IgxAMd4dmW%2BFswi0%2BZMq3ANhkNDQmhNtvF09PeXaldxt23dKcEg21DkxyL4doEe8r%2Fd4WlGyv8TUEEpGh0TKCB%2FG73bPgGibgLU229kFA9Wkw6YV0Om4UuGKw0Y9V0fjlfqHjWj4m6Q4rf0Evq%2F8V8qs99tJhwRohOlH5EaBEISkNSAJ48tkB%2Brd4IzOX2reK9Ftpc%2F5PWEymZ2TQkrjmOUXJRx%2FB0qfMhsIdbgzBhqoTsRZtIjeVoQUbneCL3BhhOd8YXlM1mQqU2L%2B%2Bxmcmfd5Z5S0zImt2Lmq6tBIDhB6vuwezf4TZPlthtt4n4C%2FiL0XF8t56JvX%2FvWzE4osTk9s1RprB5eeNjCzh%2FX3Nyh7O9WOfD7K7uZNAPFlemxdlmNdfj6W4Rhch953uTo3VCOSz%2FJveklgeA2SkgtWCDOeVU9vFG1SfA6Q7ILwWTRc4ygQy6vnNFJCEUzNgUwwh%2BwUDeU5P7julzznpU3XJXi3amdZVdzdo2%2FUhD%2F1F3nwQbJzjcMaWTfxIyyeqYMmHptVIsejgh%2BEdNcfCpQHJ2W5fNg4Cf%2FCpCQQzDGljfHTZ2kw7yhy1G05bI92Tn1CZuycRekc8SXe%2BOQPmlVNLjm6GNwqJLNehnhcbaNo4ABj7xGfqtFroq%2BFS847bTDmvoa9BjqkAadtWATA5%2F5OAHkYRvhvWsXkCrEaf5lfRTHRF9UcsmPn8BPokU8041wDC26DZHGImfRMXN6G%2BQrYfYbPK6w1UtqAs5q7HRFC7WFjLy6K7Sgh6kyjjL0LZBcJPMJstxQ5EhLnUvt6QsK5JmKGjkSWV9q4cdU9nNvLulun2Zj3ud22%2Bb6NYqHFP8fNANbq0edOQYVj6OMhimmYBm1FT9kplf4Z1s8I&X-Amz-Signature=e2b1d778dbd9c98c3994ce79f89efa35b0b69072ef18c6616e3266330d09bf32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4URM2OH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCW%2BeeONmsbTywxUxq6JzkABZIHPKRLQ9RS9UXGVLU0LAIgK5Bfp5mve%2BHtqs%2F8FsxH9HX455ij%2FhZTY54np9%2FAey4q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDL%2FlNHeVflln5AoaxyrcA1piIxeyYMV2XRzEmur7s8E6HPVWewHn5X%2BuOwdsveJLD5SQLWYj%2B7tk7skuHqoZSiZfWK1t0IYxsiJVOd0vkClKE%2FONEav3szoHUIEkU9jFfrIek2Z%2FJHTPDL05JdLW4ENLQO%2FgQf6g1E5FXNX3CijjBXPcb7mf5dPuvAe6v%2FoMfYJGZByXhQvTCENUELu%2FEf4eqldL4rMJZzKDhCOM5%2F%2BQ8yKRqF2AMg6A9JAka60Eok%2B1mc6kcCOuC%2FzJD88Khw8z3Ol7hnIfxWVTkNQr8Dxby9LCRA4c%2FjMmkEbIOdxUHtPfDfSNgZXS0WnywuslQIJuncJyKy2NscaBsEmdXq3mMd8qgHA1aJinESp%2BwcJ9oIzRoEh7WfXcZGw7PirdpRgP%2FPhZaL3gLPoOdt50pTS7qXNxYu7B8oG9%2Bbz%2FqfaF55OWNNwe1XCSg5mqblT8nmvoNnP%2BXzhH7WIMGwA%2BtaNnrvItEJGtzFn9zrJfrODNK3vXTwhpPzW6bYZRPIGaTUxVzFJ66aj1xcBlUWJmZkblzmXmJp1JIwJE6wki6jnOD5wRmMPgPKjXIEMh8HW0Qkn7%2BFGb7AHUIjfkAHvbYQ2cYm2D7HCGLS%2BDpX%2BtfLqKClpukZSvLThssoUNMIq%2Fhr0GOqUBM9yj8cfQ4DELfbcY5ySRT0lkcDOE4uCwNF%2FpB1ydIjDoL3ORB2C0vpTyF%2BNcq18NfA%2BnhveJtLCqbtdQRYDcqHXUIPLAAHO7LCl9OMJQvaOh5CiJ3HjFYZReFeXr8k6azVzXMH8H%2B7857kLHkW5KtaBcBO8Fa8qTj1h84PEfHjpoFKvGxt9ZNhglR48iPxNcIpSL6gZqT%2FIV4h40hxdIzH0ixdF4&X-Amz-Signature=0239a65aa1ecc3bd933301973ccbee7fd07f6a3994ac5fd45765ffceebdd9d06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MA6MTNX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIHlFTezbTs5hvPvTxAfB2kJN%2FMGv%2BDkO6VOqc4VbfL%2BIAiEAgZJ4hoD3bxylXLFpKPgYCh9UlOMMbdzkpedFcZplAogq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDOM6svP4PMhq%2BpouISrcA8i07h4i0UE97u5X1FgTOQNAnOmeq%2FwbkToi8onWu9zZCE2R7EJk3sEjqpkCPZBTjhIgMlarfqQ4PFDMVEgoZFGy%2F2pKEVj50iC%2Fy6bXY%2FvRpboy2qD901Zb%2F4GbaV9XZRaT0BWzf7aLTGwa52asjZKntnls8KF3ii4ki4N14JYf4QDudtp18lwM2GQU73%2FzOJw%2BBWouWnyAlCbouHt2jcGs9fa%2B7KFdHe58wJytA121PvdZb%2FsnLWQzttgodkndXj6Ot%2Fb5j7%2B18tGbc6P2sadSkuWN2RqoJW%2BpFOtSiA7hyJUZbSgK0EaRw4sTzcfGKVCEx%2BOqlq8I6iFhtqxFvd9rBwJUopit0NW6hP7TTHJwGu6%2BwfHAr6gZJ0IBp4ykzbnalCqMh2mfqq0PFVUVe21hoKOEZC%2FK%2FL6W3Ih32PIbYbTXft3DTxcj7kmZrGt5eCVyuhX6YTpQcai27f2czhId7yGQVNYQkd72LoavG8OcEex5zE3FVntgAMk4mbfbxyOSY23fVBjlOQUo1VrWkEK75uiZ50%2BGHnXaG%2FZ2pxLQewVAuW5mISiDSue2AlW%2BkrOjJMQzVKDNXGjM4oGS77vVk8KckcQfsxh10fz0OvHcD%2FcRNZrSOm1tuu16MNm%2Bhr0GOqUB9Zc3Xi0LgF1UJtwEZJLiAKRtSJlDP6mJHkkY5cAFc8rc7A%2FFrMmxrgEn08bmDhM88JOTdPGPp1Xw2mFKF1PQbi6wcpsY3SHjLpV9GQQu2RE35nTF7Pv%2F8gZvcKvhWW1TZ3ZM0XICIrfWmbtgcp1uUDUQnX8HCc82Re79%2BrHdPtwpdMQfqM0gtP1KZuWS7gWE04IIjlaMPvxfvgrTt4RZWtwK4dgh&X-Amz-Signature=f67ba9f2aadb82e6d831800db56c3c3248143a3c102c3c594801dbc92312ed44&X-Amz-SignedHeaders=host&x-id=GetObject)
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