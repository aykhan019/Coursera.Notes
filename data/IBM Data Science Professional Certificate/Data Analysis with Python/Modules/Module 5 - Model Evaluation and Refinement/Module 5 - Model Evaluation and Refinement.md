

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=6cc8f2d8f08783f69d57695d7221a2cfe6e2e92108a951c210456b018932bec6&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=2862a8648aa023cd924faeb2b99ecc162f103755b95ad94454e2399deaddacec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=af4b51cb1c7abd5673a2374016a55ed8ff5deaedb12469ae66c42ead4c411add&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=1ed524f92cabe242079703b2c45dcc31fa393f2597f9f3df2be1214354c8d4c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=1d620e80416d1f44fa857c5acab03450b8359fc792a3e811d2d448a854dad35c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=4ce2042d9e7cbab096d99dbc697859f6add375a1436270bdef997ef51d009414&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=1f58b499f14d0c67a6378a55da26baf9cc043e81ac1b67ce39db093f98abdb61&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=a7c2ae3e8264ada6f7a5558d771550f437edb2abace4f4c034c63e0a9de33841&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=3da05d63b75a80d6cd5e7a73c5df47c2aad33aa5108ebee7389e349b31903eae&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMNYTPYG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCICJA%2B4BjwOrD0PtG5tiYJgTIq5Tk5NkL0KjlkYTpjz0rAiEA9wGwTDGKhU3keX3qNb6Nz4P84yfa4sja4tSy0i03XFsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDH1kEy%2BbrDFP2Zq63yrcA02z%2BfuXODAD7h9mVbP4u5ADgcj1BQDRNOt0wkPc2aWWxBUvhHtu%2BCOBntrQbzOmsTZV%2BjVhrQLqf8E4OjWa%2BDLAtfa5M35418aAmIj6XYEl4RPa2w2ytwmSlK%2F9Z7fRnkBTcq9k4pfZ%2BkuJ7oCAONpXBwZGnO7FyOaFneZm0BXlaGFN%2BMy%2BFuTsP%2Buam%2BRCiUVO9Ub%2B9PDyNyWBIqaPBcwSf6%2F8vbl29cZ1iQhjdCMnVg8Hs8bGPAbumdMIg2M%2FN2STt85%2FK5DLKn%2BEyjYC4AO%2B%2F3ZbogRWwHwfCNF6YeTdsIg1lBuo1gTHA5KjjBq7WIYyO4V%2ByKx9QDJA2NChfV1w9KI10MhNxWarjngg9ggk4bH4EuOJaAZPG%2B1Ib3LNaNpwjgonPCDgUVcBIWAsmgmkHgTw%2FG%2FySozUB8cZZOpD7QflWO8JQbtURUicod6BODh5AW3wumEIZmaARQNJWoajSu5Fle3SRLAaTetAwOiYkiFuBVJmYeOyi57rFIOjLupXo4jkQXO2IEvkP9V3fAvto%2Fld1j19SUo6wP9FmLTQM%2B3F133pyCoNSf8OU3F5J7hYHtWvutz7UOn6MDOjuCQLNuzVGgfUGRGDkrkF5An9vLnTK2YPi9rOC8qpMInskb0GOqUB2nXAvUT66sqvAFN7%2FDnE%2BHdgpmcW7ooGCI1SjMUIoBeboKSbNVrD26%2Fih0jzIe5PZvyJ6sDUqCLWrNiq6RlOgh8O5KwB%2F7kffXv5gzu552oLeUycphJuTAJOgsomU2sGTm7cR2W6MPrbVWFTYm5nFYIGA8plTdI4NxdYDenBglEwux%2BUb%2F601DVotcY6eUJCH%2FFftWShzGokjCwdRtQ0eHRUGcOc&X-Amz-Signature=84b0c782f3334dd4ab0e29a3022fd3e86705320a4d45d2bc7eef5e7ab632e820&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMNYTPYG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCICJA%2B4BjwOrD0PtG5tiYJgTIq5Tk5NkL0KjlkYTpjz0rAiEA9wGwTDGKhU3keX3qNb6Nz4P84yfa4sja4tSy0i03XFsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDH1kEy%2BbrDFP2Zq63yrcA02z%2BfuXODAD7h9mVbP4u5ADgcj1BQDRNOt0wkPc2aWWxBUvhHtu%2BCOBntrQbzOmsTZV%2BjVhrQLqf8E4OjWa%2BDLAtfa5M35418aAmIj6XYEl4RPa2w2ytwmSlK%2F9Z7fRnkBTcq9k4pfZ%2BkuJ7oCAONpXBwZGnO7FyOaFneZm0BXlaGFN%2BMy%2BFuTsP%2Buam%2BRCiUVO9Ub%2B9PDyNyWBIqaPBcwSf6%2F8vbl29cZ1iQhjdCMnVg8Hs8bGPAbumdMIg2M%2FN2STt85%2FK5DLKn%2BEyjYC4AO%2B%2F3ZbogRWwHwfCNF6YeTdsIg1lBuo1gTHA5KjjBq7WIYyO4V%2ByKx9QDJA2NChfV1w9KI10MhNxWarjngg9ggk4bH4EuOJaAZPG%2B1Ib3LNaNpwjgonPCDgUVcBIWAsmgmkHgTw%2FG%2FySozUB8cZZOpD7QflWO8JQbtURUicod6BODh5AW3wumEIZmaARQNJWoajSu5Fle3SRLAaTetAwOiYkiFuBVJmYeOyi57rFIOjLupXo4jkQXO2IEvkP9V3fAvto%2Fld1j19SUo6wP9FmLTQM%2B3F133pyCoNSf8OU3F5J7hYHtWvutz7UOn6MDOjuCQLNuzVGgfUGRGDkrkF5An9vLnTK2YPi9rOC8qpMInskb0GOqUB2nXAvUT66sqvAFN7%2FDnE%2BHdgpmcW7ooGCI1SjMUIoBeboKSbNVrD26%2Fih0jzIe5PZvyJ6sDUqCLWrNiq6RlOgh8O5KwB%2F7kffXv5gzu552oLeUycphJuTAJOgsomU2sGTm7cR2W6MPrbVWFTYm5nFYIGA8plTdI4NxdYDenBglEwux%2BUb%2F601DVotcY6eUJCH%2FFftWShzGokjCwdRtQ0eHRUGcOc&X-Amz-Signature=af19323df2a5947d92b33d569423893273ea5e69a51fbd239a30a306ea295920&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMNYTPYG%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCICJA%2B4BjwOrD0PtG5tiYJgTIq5Tk5NkL0KjlkYTpjz0rAiEA9wGwTDGKhU3keX3qNb6Nz4P84yfa4sja4tSy0i03XFsq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDH1kEy%2BbrDFP2Zq63yrcA02z%2BfuXODAD7h9mVbP4u5ADgcj1BQDRNOt0wkPc2aWWxBUvhHtu%2BCOBntrQbzOmsTZV%2BjVhrQLqf8E4OjWa%2BDLAtfa5M35418aAmIj6XYEl4RPa2w2ytwmSlK%2F9Z7fRnkBTcq9k4pfZ%2BkuJ7oCAONpXBwZGnO7FyOaFneZm0BXlaGFN%2BMy%2BFuTsP%2Buam%2BRCiUVO9Ub%2B9PDyNyWBIqaPBcwSf6%2F8vbl29cZ1iQhjdCMnVg8Hs8bGPAbumdMIg2M%2FN2STt85%2FK5DLKn%2BEyjYC4AO%2B%2F3ZbogRWwHwfCNF6YeTdsIg1lBuo1gTHA5KjjBq7WIYyO4V%2ByKx9QDJA2NChfV1w9KI10MhNxWarjngg9ggk4bH4EuOJaAZPG%2B1Ib3LNaNpwjgonPCDgUVcBIWAsmgmkHgTw%2FG%2FySozUB8cZZOpD7QflWO8JQbtURUicod6BODh5AW3wumEIZmaARQNJWoajSu5Fle3SRLAaTetAwOiYkiFuBVJmYeOyi57rFIOjLupXo4jkQXO2IEvkP9V3fAvto%2Fld1j19SUo6wP9FmLTQM%2B3F133pyCoNSf8OU3F5J7hYHtWvutz7UOn6MDOjuCQLNuzVGgfUGRGDkrkF5An9vLnTK2YPi9rOC8qpMInskb0GOqUB2nXAvUT66sqvAFN7%2FDnE%2BHdgpmcW7ooGCI1SjMUIoBeboKSbNVrD26%2Fih0jzIe5PZvyJ6sDUqCLWrNiq6RlOgh8O5KwB%2F7kffXv5gzu552oLeUycphJuTAJOgsomU2sGTm7cR2W6MPrbVWFTYm5nFYIGA8plTdI4NxdYDenBglEwux%2BUb%2F601DVotcY6eUJCH%2FFftWShzGokjCwdRtQ0eHRUGcOc&X-Amz-Signature=3cf46e172c6aedd8aa7d6cae93e016368c04bc1df127229ca43c2cfb0f3a3730&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=aaaf46a0bd90c390096a8cd8b77d215a4b02b72accf8b507840ce9750e33e106&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=28d34d6e82cb8467f5ad6f15d8a731da4b21ec0eac06623112dbb07ecb990e2d&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=c433602e9715a52d91a9857821d669c9687ec00337f83df95910df799cc256b6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=8d35c518d14ae6be3c7f6dd20a54e3f7a85d1075f38ba32390ec8ba549d3356e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=40b20b7efd2d92a56aa0d61d2c727be2d7fc8342a421183ef775bba799d2f1f6&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3LEMK4E%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIHJQ9q%2BF9Vo%2F7xakA6rZBK3eDMpGh6IA2ZDfNy%2BQA7YDAiEA3qfBeuE2vTTprL4NU3KT4ZJdlwsEx%2BQLBoNmLaqPiIEq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBoabs1A1e7%2FlwQ21SrcAxZ4LV2QVvncPKej4yRj0WLeusIjs2KN7xD0RN%2F8gQLzm%2FTBhUIzWTrAZ%2BhR2DAVl4BeBkHnty3vQBmKYrZAhZpvs706PxPHnzj1DZxkKn2wMPNFsZlLV0%2FiOmwPMHsqcx4u3AuwBmPrKnK4UIJLldBWpvpwYP4QV4P0IwawUHCkxS5IMbqoeS2fhMdho%2FC6ynRDiMM14GhYGXs2YfssnmRzKunv5ZjXDZE%2Fxj%2F%2F1uT58nvSMcnSHn3AUWfFZiA4Ltim3rTma0W9I8Pk5uIhuY52YvTASvvQ1NBNuSQNTFWoWWPWNJDonL9vfruy8TLwa5shVtLpwyEPUDWcNMU8iXPCoz4L4wr5sN3E8Img4QB5M%2BlJMv%2FDRwdcYpy%2BnPFOYUlBVCGjnDuzJmi6jAcF9LmATWNCxen0l8CK8P%2FlTEctECA%2Bjj3uZMeL8dy2TFEPGRfIGcI%2FKL18NJYg0sjj3LasXFZutLJ3GOKoj%2B1DrWPmm2%2F87Ll7k4PTmw10IfPXtV2FSU%2BvCL1tsao2Vglt2JeiABxZWpN%2F8vmWuMvMciV8%2Bp44vSbNSvXp%2BDrvyZ8ewPt%2BkvMs%2BNtBi3L3Ph4AxqY9e9vzpssUU%2BBJIAlApiaPj4Do3LP3v6aqn4%2ByMIbskb0GOqUBKhAOZ20x8uLv4HbNfA7qArLoanh%2FCBPEC6KsTzii7FCguJ%2BeCrMHRrS7BZ8qlE9N7L%2FgReSeSqF9C%2BLeozE5Goshix2DxEyP911xgryrDXot2oo5DuLm08zTm8dNi5aT2sOSBTbtJGSiAQrzy27mEaHwcdTRaxOLRUUr2Ea8EH9zIu38GgtARh3MDHSB3%2B9HD57kyt0hhk9IDJGMXMm7Ic5aYPNV&X-Amz-Signature=69c5e5799de24399aadf353f20c320a7c9d2cb3e15cc1427f1da27fd06e73c5d&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6WON435%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFPHeowtTFewVFsfheVYsYtO1wr0nRgLVMKhVVmOAqqyAiA3hiI8zau9HtijanLfqFRSTXuZMHFJYfDR%2FS2yM3i6Uyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMZrui%2Fsfu7%2BBeamlvKtwD3Qq4wNGlJV3Murp65WvkWaCIOJnDfE7JzhcUJpbbP83JQMlxQkNEYq73z8cP3YyzEcxjBdRBPflzXegS%2BQT9BzYTDUTWDg5nf8jL%2FrL8exRJNMB%2FbtP3zpMLu4E92Q7sDuCATr%2BdiPuDED%2F3Oh89GTL4RYS7KQbjLU0hE%2B2Pp2MvQslDcc4n2xho8mTdQLtt7gcbsb3s%2FoY4TReVOIpwGi6uYrrUicoa6wPjGSNwLTFp1SJ%2B3jIILhzx%2BzSZmpTs1p%2BKggyDf7Ry59ctv1moiAsRsmA3g9x%2Bxv%2FFmLt70cbj4jmR%2Fc8GOCTrYtHHHqtwSMGMrpRNcnguXHNAIZ3NgUzh50hEmBkHA7Tb5NDrGV7%2FRCcYvFX7JMAe%2BK%2FwIGVTkD%2Fl7fCRnXx6ZmQl6J8MKaAXRW88pOb9WBGvBciih5Jm8oFi5Nm9VqZ3FEZN%2FywFnrb%2BZlGgweI7QEn27AVxdWHPFhidcvUSNMShN%2BPsvNi%2F%2Fo%2FGUXrzX8uKm%2B0jYwiAnX03R45vr4MdHShBHVd%2FH7pVwpOb%2F5yVHfm5udyaQVeQ3EBRZySNW4%2Fcp6Z6menW5lPc0Y2%2BVQYPVz9is5NbSPPnLdOe%2F%2BkqPa1%2BWXh%2FBcL5qm2THIfu6T95gK0wquyRvQY6pgFgpxOGJVaZ967SaWIb5cBR7vwi%2F5gE2mryVMitS5HSho9vDDR3qLzVCDO3d%2F2gap6yUM%2BRG3OutCSDX8UnhZM5WirQGtdJDTvUh25J%2F2QgQk8h5lykCtqFdR0sdJAC%2F4oMGYOS4QIZClf3V0K5HU1lYhT0yX6p7VpU6EVOmNvt4W0KCVmYt0HiH4TxYYO7ORkVKZlN4RQ9MwXStmhzsxjiEsg5xBIw&X-Amz-Signature=81c82b2952a71a21de37bebba067220aa0db6bffecdd94f03dabd977f314b25a&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6WON435%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJGMEQCIFPHeowtTFewVFsfheVYsYtO1wr0nRgLVMKhVVmOAqqyAiA3hiI8zau9HtijanLfqFRSTXuZMHFJYfDR%2FS2yM3i6Uyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMZrui%2Fsfu7%2BBeamlvKtwD3Qq4wNGlJV3Murp65WvkWaCIOJnDfE7JzhcUJpbbP83JQMlxQkNEYq73z8cP3YyzEcxjBdRBPflzXegS%2BQT9BzYTDUTWDg5nf8jL%2FrL8exRJNMB%2FbtP3zpMLu4E92Q7sDuCATr%2BdiPuDED%2F3Oh89GTL4RYS7KQbjLU0hE%2B2Pp2MvQslDcc4n2xho8mTdQLtt7gcbsb3s%2FoY4TReVOIpwGi6uYrrUicoa6wPjGSNwLTFp1SJ%2B3jIILhzx%2BzSZmpTs1p%2BKggyDf7Ry59ctv1moiAsRsmA3g9x%2Bxv%2FFmLt70cbj4jmR%2Fc8GOCTrYtHHHqtwSMGMrpRNcnguXHNAIZ3NgUzh50hEmBkHA7Tb5NDrGV7%2FRCcYvFX7JMAe%2BK%2FwIGVTkD%2Fl7fCRnXx6ZmQl6J8MKaAXRW88pOb9WBGvBciih5Jm8oFi5Nm9VqZ3FEZN%2FywFnrb%2BZlGgweI7QEn27AVxdWHPFhidcvUSNMShN%2BPsvNi%2F%2Fo%2FGUXrzX8uKm%2B0jYwiAnX03R45vr4MdHShBHVd%2FH7pVwpOb%2F5yVHfm5udyaQVeQ3EBRZySNW4%2Fcp6Z6menW5lPc0Y2%2BVQYPVz9is5NbSPPnLdOe%2F%2BkqPa1%2BWXh%2FBcL5qm2THIfu6T95gK0wquyRvQY6pgFgpxOGJVaZ967SaWIb5cBR7vwi%2F5gE2mryVMitS5HSho9vDDR3qLzVCDO3d%2F2gap6yUM%2BRG3OutCSDX8UnhZM5WirQGtdJDTvUh25J%2F2QgQk8h5lykCtqFdR0sdJAC%2F4oMGYOS4QIZClf3V0K5HU1lYhT0yX6p7VpU6EVOmNvt4W0KCVmYt0HiH4TxYYO7ORkVKZlN4RQ9MwXStmhzsxjiEsg5xBIw&X-Amz-Signature=ecb42bc53fcb19afab0e5ab530e614a38a909120e33fcc8fedf50047755a7d75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623XHVASK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDG%2Bj14BwbqA75MNnfvyOsO7JyD0zgGKrcoJHzFQIdIHQIhAL%2BYdJlVHHshHDG1htq5ke%2FsR43AkwYYtQPAJ53Q2y%2FeKv8DCFoQABoMNjM3NDIzMTgzODA1IgxfJ3YCgmr6uUKPW7Uq3AOuIrRKYzUwR5Bu%2BBABEyjxkBC%2BKSczAmYW7DkqSsXzGNVc5%2BvebFetwiwMbGKxjXKlsAs85tB0o7Y9wm%2FXqlpef7qR7DeYQTZ0KU5H2vYX0bHN8BnJN5C2j%2B%2FaSREYU6O54FryturwykAXHgw4%2BROdbDYgZqG22MAX4LuzVxSrNGBZnePLlaliZjBnwu%2FJCG9AUn0Do8yrn6cQKCM7qlZuRQJlAnT2XxDxUzzgWO15E8drNJVxr0YyPQMicpZFxNRkwF1Ef45BZfR6ZzZI5H3uPTC09aR9Yr%2FZTCze5AJPuAmu0PwsByjyoC9bAVYW%2Fn5IhrJr4ejTWx29ngTBGOt2a0rrWiyofRY6lpMA96eHcEr0tWjALEYTTQVBddf4%2BFOeWE9HxfF5CSxBBQHPjtBHLER4iIK98YfxxNEYX9MWTSjYXeTmGcSCFjAiJiaQaWgwMLZc8QVtntDTmLU%2BzHVTqyBIMaf39SpNswloz2e9kunaLsAzIx0tVB84T1l9POrkycHoSHuXTwLYCUj6GL0wcpHjhclrpdW9rwc6oOy9w8M3jOjT4i4M6djcFz%2FoKebXPancNeD05Z4%2FNTBrbJXH%2FTJr5oqZaL8O10YYl%2F9rHXYhjc0s%2BICPm7rakzDX65G9BjqkAcnRZotX22j3mdQp93LgOnUS3zmRn9QRj8RxF8kHUlqhDlvlczIjqB9ffPFLOqURVq0eeIFOITOZCIjc1WbbOL5inc6Oxovsed7Ri8A%2FsrZ%2FFzbkgpPjisQ6ulnYLEstRMAE8xUqTP5U81pwoxJsLugGczrte9Okf4v2QhfGC4It9NoNeKEaZCZxJyzTwjm4m3p5HxF2xOs9t1uNSLqex59q3wcL&X-Amz-Signature=5ad9e4ab373ecdd728c92a7d03fc196f0c5211ca215f8bc6eed2d2a1c1aaa3c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BLJABA3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDsCnz8ZefcmNArBJrgqaBlAk6okhyx1limbygAWvWEJAIhAJOWvpRCruYNCgNrfyRYXiEtSU0JkkyEotu%2F%2BhrSL6ImKv8DCFoQABoMNjM3NDIzMTgzODA1Igxyq4qkLbKA%2B6mHRKgq3ANRlMqcE2kOChvbMGArUXNwWk5T1ONTC4yrmqlQE64nsQPPm0J85XG%2BHia3ir0FYulpu%2B09yEjxl9iTJPAiHLXKUURAvDUrEz%2BybMUF%2B7xhCVCDsV8PFbrcpQuI3SONipLvkX6LNKF04TdV0dsA30SI4lTPHMda%2B2zcpKBZ1egP1024rfauxOS8jGa9BjBArC2JULcPUnHMBBII8D1I1naU7hkBoZheY%2FiwJoCBA%2FSrQDotz2q1d1MIIimwRdod9Z5GZwKX0cem94CSDI0Fne7uGKEkBmcdaQjv1xPWVZUTwq2nPftLrapjuK%2F3oC%2B2UvIhP%2FIEUYCRz3dloqYEvY8Ofor5uAfpgZ58KAIqSeFrY6dgKNpmeIGuDdB3%2Fz7lCC1fOW%2Fs%2B52NOClSD590AszFXsFhb6jWmoyo6G03vDD34Okmz9%2F3PPpanImR8am6ii%2B0OzVT9BCLfcqnFI9KxqhYuhzF6nYECRPnwf6YcmGUVKHJg1pBCpRiTFseUY0aH%2F36DLxLd%2FWs8x3aiPZ6zQuX4oNCxe%2F3VzfQTjoc71XIcN9u13gvFbmkE4sCWD67GjoPqlvm7NxpPvxiaNmbjtMG5eORW2yBSUjPWblASIUyngKtg0KKgS%2BdO9Yj0TDU7JG9BjqkATLd8BbXUa1GlblAqZpfult22WqBiivZDur8KyulDc4HK7DVGT3AlK%2Bt9RhuO59CjO2cUo1ByxMmd5zZ0vfwmHAeRXHUEhmuIfiuiXhFfMPxDhFbx3s%2FUa1bvzgs5N52FwOc7W20CurvdJjGHSsVHoB62mSU0ZSFBBuxRn6ZuiBuSKL2zIAAp%2Bko2erChYXYrv9cAsf1F%2FBFi2gAjJaD8yKQFfcu&X-Amz-Signature=0cbed2b01b8fdfb7e83ebf15ef2c15d71a4394ae55d182208a5f05e82bd64dd1&X-Amz-SignedHeaders=host&x-id=GetObject)
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