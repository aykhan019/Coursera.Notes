

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=0797ed262942acc86d409c837d1df4364a4ca68532fa468bdec77b08a5aa6899&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=d7930455015b494debb8d6f9011205dd0035a1236b75303f20506b8551a01427&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=1ee3c74bd6bf4e7c72479b719e6f1f336336a468d36c5a17a67c05ad555cd9d9&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=8f14ec7f16122f09991272ed25b76b6d14ff1d412d5f1d935e62b22a94c8ed6c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=6709226dc11c0c9cb28a0fd068c74882a1603a4f7f7ae46a03e4059e7ef0cabc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=23c500091e6e15131362a5f77def9999a0c3ef85c25c223f77f6b1c2653284f0&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=abeb024635ed42c51c571da9c3e22e25eba50ebfaf394786025a29c3290c5bea&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=be96391fb37b2b65feefa3807bdef1e25c8b0b5867cdb659ceefd264aa7574b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=8c9973a18160a69fb693b37b9fb489c7f0a7cdedfaf29e50394bf3dae482e063&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G2CKXQD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDoiyMY1myZNPlECGM7ntp9gOB1RhBP6NcF55gqTVRTCAIgXsQdYBVP9cVVlhJlMKCNV2xPRapqR%2BLg%2FHfBIye9jeEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHLtbUB9tostkXkdgCrcA3gkRjqVuCScHVXALklD4zOpQBMe5UQdJk7iou%2Fp4xdQGHLaWbeKTfV45Rij7YsSEpWomal9s54DcKfDoUQ29tXPTNRLtCxKt%2B5aBo68xrplqVseJPc9pXgkSJTMCrxN1qleDWwqmSiLuO7ohg99uNIuAZ%2BVuIOt%2FEFAofNm%2Bo2HCB4%2B7qQYUmSbPLCWxSEYTBecB%2FIRXqOCDjN%2Fm0LIJsEp8wtIX%2FLC4gnNfqxSPRErDe9%2Fa7tC1T5xElUgWd6iHpbN4bbfFxxpEojCgjAcRC0Hnck2EDrsA%2F968K%2BkeCT%2FRS5BhWqCAmsY3eiZJ7VuSZkxBorPJtOWi9tqayPf0gCDOKBcvAaaN8N1QbPKdUOhiqW9YjwHyq2v5lh66B4tOn%2FcI2S0rChvUSwrQ7Yd4ErunKsm5cWnKEjpx0XvNVGaNuOPUvMq2sP8yVePUIXuTMWnJ2%2Bgzl%2Fx%2Bn9Xd17XP1hPhcnRD7OgizujtHq8usK7Vwx95qx7VEDtBfXEOSgYPHLekFpRdcnMlJn%2BYCJ2VcplDwgP85XXelAOdCJ%2B0KhcuOWoHe3zJJ2GiCzHienG85sonV4ABmYqk%2Booi%2BJ%2BNJwjthHplRjj6ev5jVgtXM%2BJ3Afm78Oa0bfo5ZkBMPOKmL0GOqUBOEqbwFWgvQ8ajVjaoi7rzkRhV7SulPMP2xV0svevBU6RKUonyTWz7o7zsJT11usoAiO%2BrWBdOhcTa8cy6W4ArDIfNrRCXrpoZ33zvkoe0AcmNbB07jHsioj0rhYNH1qeJ%2BC%2FhTvGjNnmsuvZa5eUw%2FdF8uYw3v65OnvxKOx0KTbRDGh%2FHyDG7QI4kBH5VGxM65Xj5%2BTepA5cmyw6kROWV%2Bqer64r&X-Amz-Signature=7506906f7335d0def3aa8676ebb667cb94a734b4f399e90fe136f4d4b9b87171&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G2CKXQD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDoiyMY1myZNPlECGM7ntp9gOB1RhBP6NcF55gqTVRTCAIgXsQdYBVP9cVVlhJlMKCNV2xPRapqR%2BLg%2FHfBIye9jeEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHLtbUB9tostkXkdgCrcA3gkRjqVuCScHVXALklD4zOpQBMe5UQdJk7iou%2Fp4xdQGHLaWbeKTfV45Rij7YsSEpWomal9s54DcKfDoUQ29tXPTNRLtCxKt%2B5aBo68xrplqVseJPc9pXgkSJTMCrxN1qleDWwqmSiLuO7ohg99uNIuAZ%2BVuIOt%2FEFAofNm%2Bo2HCB4%2B7qQYUmSbPLCWxSEYTBecB%2FIRXqOCDjN%2Fm0LIJsEp8wtIX%2FLC4gnNfqxSPRErDe9%2Fa7tC1T5xElUgWd6iHpbN4bbfFxxpEojCgjAcRC0Hnck2EDrsA%2F968K%2BkeCT%2FRS5BhWqCAmsY3eiZJ7VuSZkxBorPJtOWi9tqayPf0gCDOKBcvAaaN8N1QbPKdUOhiqW9YjwHyq2v5lh66B4tOn%2FcI2S0rChvUSwrQ7Yd4ErunKsm5cWnKEjpx0XvNVGaNuOPUvMq2sP8yVePUIXuTMWnJ2%2Bgzl%2Fx%2Bn9Xd17XP1hPhcnRD7OgizujtHq8usK7Vwx95qx7VEDtBfXEOSgYPHLekFpRdcnMlJn%2BYCJ2VcplDwgP85XXelAOdCJ%2B0KhcuOWoHe3zJJ2GiCzHienG85sonV4ABmYqk%2Booi%2BJ%2BNJwjthHplRjj6ev5jVgtXM%2BJ3Afm78Oa0bfo5ZkBMPOKmL0GOqUBOEqbwFWgvQ8ajVjaoi7rzkRhV7SulPMP2xV0svevBU6RKUonyTWz7o7zsJT11usoAiO%2BrWBdOhcTa8cy6W4ArDIfNrRCXrpoZ33zvkoe0AcmNbB07jHsioj0rhYNH1qeJ%2BC%2FhTvGjNnmsuvZa5eUw%2FdF8uYw3v65OnvxKOx0KTbRDGh%2FHyDG7QI4kBH5VGxM65Xj5%2BTepA5cmyw6kROWV%2Bqer64r&X-Amz-Signature=e4ae1f6317c0e8ef5abec812c76a721d386caeef52920e96c55a36ecf8ee092a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G2CKXQD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDoiyMY1myZNPlECGM7ntp9gOB1RhBP6NcF55gqTVRTCAIgXsQdYBVP9cVVlhJlMKCNV2xPRapqR%2BLg%2FHfBIye9jeEq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDHLtbUB9tostkXkdgCrcA3gkRjqVuCScHVXALklD4zOpQBMe5UQdJk7iou%2Fp4xdQGHLaWbeKTfV45Rij7YsSEpWomal9s54DcKfDoUQ29tXPTNRLtCxKt%2B5aBo68xrplqVseJPc9pXgkSJTMCrxN1qleDWwqmSiLuO7ohg99uNIuAZ%2BVuIOt%2FEFAofNm%2Bo2HCB4%2B7qQYUmSbPLCWxSEYTBecB%2FIRXqOCDjN%2Fm0LIJsEp8wtIX%2FLC4gnNfqxSPRErDe9%2Fa7tC1T5xElUgWd6iHpbN4bbfFxxpEojCgjAcRC0Hnck2EDrsA%2F968K%2BkeCT%2FRS5BhWqCAmsY3eiZJ7VuSZkxBorPJtOWi9tqayPf0gCDOKBcvAaaN8N1QbPKdUOhiqW9YjwHyq2v5lh66B4tOn%2FcI2S0rChvUSwrQ7Yd4ErunKsm5cWnKEjpx0XvNVGaNuOPUvMq2sP8yVePUIXuTMWnJ2%2Bgzl%2Fx%2Bn9Xd17XP1hPhcnRD7OgizujtHq8usK7Vwx95qx7VEDtBfXEOSgYPHLekFpRdcnMlJn%2BYCJ2VcplDwgP85XXelAOdCJ%2B0KhcuOWoHe3zJJ2GiCzHienG85sonV4ABmYqk%2Booi%2BJ%2BNJwjthHplRjj6ev5jVgtXM%2BJ3Afm78Oa0bfo5ZkBMPOKmL0GOqUBOEqbwFWgvQ8ajVjaoi7rzkRhV7SulPMP2xV0svevBU6RKUonyTWz7o7zsJT11usoAiO%2BrWBdOhcTa8cy6W4ArDIfNrRCXrpoZ33zvkoe0AcmNbB07jHsioj0rhYNH1qeJ%2BC%2FhTvGjNnmsuvZa5eUw%2FdF8uYw3v65OnvxKOx0KTbRDGh%2FHyDG7QI4kBH5VGxM65Xj5%2BTepA5cmyw6kROWV%2Bqer64r&X-Amz-Signature=d5b3fbfe58e8ea949033731ffe4d15b8f9eb104b49fe4c6270bb09098c4b8c07&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=e2fe60094d014b7a18f9c17f93e91daa1b7edaa6127568c59c635cbe2c964297&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=d69bb2b4d1f4af7fb6d6168c9e324c7caf9d2ab27454c1b0ccff8c0ab7d64c39&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=9458a3ae5b244d80418047eddf4cf9691b630700af690608d576a8d3c442114c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=4bc6e38d231263ffc1e53cb2716bcc7819e634040ba145c8c665ff1a1bae4fd2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=af7ff41541d67247046da8f79b88ee2fc578f9b0ec11c9bac6eba1b13407ffc6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642OOMVDE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCIEVmB4t3XJU9vqXLPRS4RKyDjcGk7Jqj4hwAecfVTztHAiA3gcDrDDDkGv4u4gn0D9E%2B98DlodL7G2MdzJR8S3Z73ir%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM2X0svYE5Z0PRx3VGKtwDv9OM32OQLWT5wVTeUWYC5Cv3dl8xdvfoaK%2BpdrroL448HrNjbPPmw0omyLGZmZQ5oI79u9wxXN%2Bo9q9JtX%2B%2BAFwlsSkLH4%2BLwblgwAT2o0O%2FfhkquxQa0lHGF3K4Si6nfurPERhq5rKCeoOn3aEJYW%2Fbf1cB3nDI8TCFET0ZTGWqtUW9ymrs5GdCEDeka3hGty6gfgM4buKfUdr84y2L6T911wpDHKaiwEhkLEjfz3uiq0TWYR4u8%2Fmdp2FGmbIXmHzJ60sNQwqbKQgs7mgTyZYIh40rEmEc5TPpeG%2FisqwCddCRKq4z1HJcJFr%2FX4f9%2F%2BVtqUYoPXI%2FeNDntoA2QhVowbV54lWv0R8nRcSvjBp9DIS5xgBrEQ%2FR4do1FqXi%2Bl8xQLJ4jYTukcrgy8Y5chjdrzXs68avlAugihQZMGWOiimdGzRf6o7p1Yvukp5gcxgyoSOWVM%2Bzn9TYgA9uPKJ7NbtRjMJK9oyMJEq6XntbscihkV8%2BYLeSLEIhGVt6f72mp%2FzXTMsdqJvZGhA7xJRbeyZ2%2FxBrdKhM2qLfkADYP3LmeF7WGR2JdPRr07%2FA3Lb%2FeJHJuRyMMOUJxFTP%2F7Tmgy%2FFQvPg7S%2FpMcHTI4s6Ek9fPujWFV2fCI0wlIuYvQY6pgGxoKb7CHEY1r00NntkpUKlmtkeOtAz8QJ%2FceD0PKJfmAn4KEow7KweN%2FWyDSg%2FH6J62sR%2BO5ILoaZGfbO6PQHgDu5KqLroZ9iF7pt9GlYUmqDc7nbfwy12IP32TIzMCz0YrUK5OQF2VpqHA%2BWpbaoxIckwT2Mi51v%2BFzyXKXCiHgUJyJx3eZi0fxkYQRosafzT0ptbtHhf8LVr%2BR0de0tNdWSrURXk&X-Amz-Signature=46c6e2969f676507eb09020c8cbc3002e1d3832f223fea27b4e7b65e838abfc4&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664755FINY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQD3ltkVFIqYJnbl5YCrrsPYWX0JZWtRxER9w7VL1FbNdQIhAIvUfnyUeRKJsYAlTvO8fklJQmM7QGCugdFxn5wVo9j%2FKv8DCHYQABoMNjM3NDIzMTgzODA1Igzu%2Faw4%2BJQ8%2BqQ2MgAq3AOAcPvrhPdFfEafnK7ur5DPNd%2F2QnsbSkqg7mIf5YL%2F6i7PO0VbjkdFPRrfH6G4DMy1Hf%2Bl22MJTJxe0QUf8V1CmXkhOrln7yJgyKhcrqn8UhmmkVUAoQTUwwWr8BR9lpEVZTIk20VjjEZRUtC%2FLVqmFqmyrUCPkszDBlx3WJqght8UZAStJNgaNBKJq1NjS3QKaDErnK%2BZA6dZZkRt6ItJtURJZJ46opcRr3d5y1pnbksgCL1rnZltUdY%2BgeP5tqKhTvf9MawF4hGwwzunpa62Depc%2Bzgwd%2Fn0aucJe58kfmXtBkqzVF4NVEoZ%2B%2BPrJw4BunFKp93W%2FgvtEjT8pnOoLIEMVyXPHQ9X1o6qftUvXrK5FsOR81AxLt310lTZqyp%2FR%2FuKy6ceIqCa4fDyNoI71WnyHO46u9MrOSH7GW%2BqhAmJCOYLczSUgzBv6bQCaZqGGUtJwZH3AbtneVw8Zv7paZT2oMr51uABejGea%2B%2FANeLZRyRB4vLzIllvVFIwyjCBtJmG3e8vVIsk96ut144Zykyhmz%2BlRvYo90VW2f6QcGIB3TuEruYp0OZMSc9QS6GC4JX86fGHoDGgBQHpfA0K5vB29WWiZ%2FihHha3tTv7QM4YuFgSDJX9d0HVGzDDi5i9BjqkAYQnmxw%2FXadA7T45mTjpHf60HlSKdKgRPxS9NY9xp6aVlaxBoE7pxf94olEuWSmU4MEI0PdWKqU5iWygJoSajOurwv8rEbKQ08u%2FqEZKAIr5c%2B4GuKc%2B7%2FhJX5Qoc7MZgJjHirFwiQx1dqU6pxD%2FBZ7082N1YnzYtW1x5J9%2BaAVfYm90szHgYxtUhHy4cEotNLQWcItpapsRb%2B3CybSNNkbbGdoF&X-Amz-Signature=132444d0ade783886488b478fbaf7c789445f31f281ef098d38e2a73d44bb7a3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664755FINY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQD3ltkVFIqYJnbl5YCrrsPYWX0JZWtRxER9w7VL1FbNdQIhAIvUfnyUeRKJsYAlTvO8fklJQmM7QGCugdFxn5wVo9j%2FKv8DCHYQABoMNjM3NDIzMTgzODA1Igzu%2Faw4%2BJQ8%2BqQ2MgAq3AOAcPvrhPdFfEafnK7ur5DPNd%2F2QnsbSkqg7mIf5YL%2F6i7PO0VbjkdFPRrfH6G4DMy1Hf%2Bl22MJTJxe0QUf8V1CmXkhOrln7yJgyKhcrqn8UhmmkVUAoQTUwwWr8BR9lpEVZTIk20VjjEZRUtC%2FLVqmFqmyrUCPkszDBlx3WJqght8UZAStJNgaNBKJq1NjS3QKaDErnK%2BZA6dZZkRt6ItJtURJZJ46opcRr3d5y1pnbksgCL1rnZltUdY%2BgeP5tqKhTvf9MawF4hGwwzunpa62Depc%2Bzgwd%2Fn0aucJe58kfmXtBkqzVF4NVEoZ%2B%2BPrJw4BunFKp93W%2FgvtEjT8pnOoLIEMVyXPHQ9X1o6qftUvXrK5FsOR81AxLt310lTZqyp%2FR%2FuKy6ceIqCa4fDyNoI71WnyHO46u9MrOSH7GW%2BqhAmJCOYLczSUgzBv6bQCaZqGGUtJwZH3AbtneVw8Zv7paZT2oMr51uABejGea%2B%2FANeLZRyRB4vLzIllvVFIwyjCBtJmG3e8vVIsk96ut144Zykyhmz%2BlRvYo90VW2f6QcGIB3TuEruYp0OZMSc9QS6GC4JX86fGHoDGgBQHpfA0K5vB29WWiZ%2FihHha3tTv7QM4YuFgSDJX9d0HVGzDDi5i9BjqkAYQnmxw%2FXadA7T45mTjpHf60HlSKdKgRPxS9NY9xp6aVlaxBoE7pxf94olEuWSmU4MEI0PdWKqU5iWygJoSajOurwv8rEbKQ08u%2FqEZKAIr5c%2B4GuKc%2B7%2FhJX5Qoc7MZgJjHirFwiQx1dqU6pxD%2FBZ7082N1YnzYtW1x5J9%2BaAVfYm90szHgYxtUhHy4cEotNLQWcItpapsRb%2B3CybSNNkbbGdoF&X-Amz-Signature=ef3e413809c08f5e4e4a9ff6558e0ec6e0180bf4f53a50a119f6a887a7773f89&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDOKCRVZ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQD6sUQw%2FAUaGJ3GgL20iONFtUdqqEMz7vGAQb3e75T9BQIgX6XiXSO0QEPiw0Mkiupx87oQ054nR%2FPbdXYVd6X%2BqaIq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDPgp9JJFnPMHEqYyxSrcA1z8EdLQUsGvmSgAAX6ktYL3r3YmniYW83cTzl9lD%2BrjFEbIySE0%2FhJn%2BO7Xtq%2FSG8RT24d3agrVkREW%2FVey5DoCm4PtsCjeS9hSjrf65MEok0xRJ4vm%2Fp69Qzrq5n6eg8wEFnRba%2BKAFrZZASLiLZ0%2FYrsP8YNb6R0QECRB3y%2F8vtzXSxdJbloU0cg1jTcJUrSl8RoUgEUwaA2fseiMVFtOOKQavynrLwyZWiBmX3jtNvlqCTX69QAtoKerYjOZHIaw7QQS52vr5e0ayt7Kemuc4JPRNhe0GJVK5CjSHP%2FsABj2rZfob%2FAi5T74PV84kPeO5P1ECEY56oaCGGgdQan47GKhJf8zP%2FGU%2BkEGbeQGOpLwbT0gFKQYkmaPxcOvNTI1O%2FR65GNcxoZWI37d5z%2FF31COQCYGtVz83YoeDaL%2FpNCkPjoXDUE8s%2FcdtUPbRSr8LG9Z%2BY0BS3VOT9R0XBPVqObqb2tzNVIZ3L8LdarfC4BKKlGdkySTpF5qiqW8hsVxry7xred5HTwopBvkIc2pamwCAfc6JW15kkGsiHokJuZBtljWuC61ZiD%2BKv79mqXNp4qWsmwMPLyjKNwefGItGSTMySjZ0O%2FUnC%2BGiUKlafjsuyETr7CJfUz8MK2LmL0GOqUBxfT5mmZlq74jWih0BpYT5sWwbast32qhHqkW7GZEF8vgD2A41aNgcusbSOHb2YMOuOC%2Bg4qxohTEx5TM3nezOYtJKy3ulBJUAbdQoZ5YPcwZXN3%2BuQeIGkArMxpCEi0brAWIZQwVx8zHE0pCwC9OnyaLphW2jJqzKdl5%2FoSfEuNSFlGuZeHS0h3yKhbsg5BwZqXliWMIf4pSSiXVwGXudkJCkBj%2F&X-Amz-Signature=71553f63c629f0f57dafa4eac8d541997481c0f0917b325de33d016db82b6a2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWP2F75Y%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIDBvMn9YZ19Q40ZP7xpw%2FBemIkNDXYccdValbYXUoNdIAiEA5fV4ZbzaW%2B3dle3i7Hy9tQCTFIdYG3oQbd8g9Rtee08q%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDCtar2IgJrSoh9SWKCrcA%2FqVWFY8RX%2Fk15aVXCManUaIrsQwt%2BVPnqmVBs0JiYd0PanKxXwkPOY3f5MYi01HlSRazt8lc4pJx%2B0UT5YzE2fQYlrR%2B5aCRCaoX1sTVJklQ30fw2NxcKF5O9PvSAcVE%2BOQ7g5otG79itb6Mrx1RtrQiRK8ck2vJU4qVpNl4qvy%2F5luG40AO1PZq5D9DkVgAUoV5kzAYH7ixAltG7AW6EztsLrahIN6aGXBtg8BQQPeWt3vTGunzDBVMsCPTx0givfoWnPkCCe7d6MauuLnEK6gEx09X07tMRzaKu2RpL5dA4Ub2%2B30mjWe8Z8hubtOVu68FvfJ%2Ba7j9IaT%2FIMGTIZ8UlNiC2ieDP3TXXgyFCdkNtIZnO6zO%2BMiukuhmA61L3ojmF7cSmAsJUbmrFW%2FJHnb2%2B3skp9VutLZ684vNlvOr3%2BsJl1DLBV2kWLdeSAt3J2Sc6sNiVBJRJ4YNZZV3rf7PRsN7SjRO50pb0iYPijhRkSPNcmc1OJ28e6YtC2gKticL%2B%2FZLAwjk74SXytkrjSsf%2BEWbk9rr7yOgGDLrsF700ZtxfrkbR6K7fA0pE91yyu0GSkUE27yb8f8U485ku1Z7aqXmxfNJx0i1eXTqJrfdAcNbxB8BFxSP9MPMOqKmL0GOqUB04yPTnqIOCXD2%2BXeWkTjU4Xj%2F4FFU9JlBBUr8QtS1GqxM1TKp6G7eMLm6qhW0LY34IU64d%2Bd%2FTJBs93fvK20n1x6kuYKR40EudBCkXu8II10aCBuJVclhspGgZ2RipK4xilQ9F8g9ACwD%2BAx9ntPyzlXArdKgL7v8jUzOE%2FbQbJmlziS9g0RxSrpodjtaQSUMQ4QscNiVNH3r%2BpwGhMOe19OpEcH&X-Amz-Signature=624dff22267d49f5e83324aa20f24f508ff27345ee874b8a7a3abce29e56a4fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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