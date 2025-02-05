

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=45e80f72a253bf9abdeffc08e2f77dea0d1757cff9402a18fbc9796569a50c8d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=7229394064b0a2fee1a2fb35c9e00b821093e4da26cc98281d92594b7d164a21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=757b42221bcc9874dee485dff5371b6039a9c98c4b366687feab6a03978c0d38&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=36e5d826265dc480eda6fc7995a945748aa03f5fe31fcff1ee5e16c1e4ec9155&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=4a7e0fbe8c4ad9b333eb28dc65cc88d4e56b9f0f5bb93c75891a63e108e6b9da&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=0d00c1b581a94184e06010104d619a764e396a4a279f27d0963b3db6ef32e0f2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=d923ae147dbda6df8e8faaf312d0be83d95287921a13e6a02d64065e643b4cfb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=aba73fd6d03404612bc667b73ed3d33c2b808cb834276f995f3ba5eb7722d6fa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=3ae6c0e822aaf45c1aa6a7b23da731b40f0e4182547cd8ccc2c1c9ac8e6ec8b2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPSS3RPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCOSDGiq0TKwFIaeXRqGNn3juQ9Ni3Rn9co2OLNyuvbYgIhAOYiPkPokXIniW6gw9KMtc8nMUEVSmA8jZFRK%2BFfiPkyKv8DCEgQABoMNjM3NDIzMTgzODA1IgyzsxysGbFog8CaeiYq3AMlxDIUYeNfCpk%2B0IWLDJd5OWw5rAXaFKWS6xEeq1qReMv%2F2eeUudoDrMGOy7xmiIGjDw9610aMo%2FFZKfj8TQ27f5zehxDg4fprupGiy2bmq8HkGTCSbsy7o8nOGpzo3C%2B4kMsaIIqBT2f9oU7cOs%2BHU94DSm6CsZMwdB3YW%2B%2FmHe1i4yCWwYHiEmvzEYmRCKCyjGaJYMhe6qYkKykqeEsbjm5kxLea01drLIVmXx3MDV33UEA3HAuaIJqXUl%2BehNQ7UkbyoJhHU%2BhQ5v4%2BHw9F1XhJq4jjlNYH6B6lDp%2FyIpUa3HabVYGtU69zQFAsG8BbQJu1q1%2Fiv%2BGLFS5QZQV%2BwWboLViKnvydN%2FH35LqXbeEVOSJ0cGa3GAOM06UQfbKl4n4JuJscLX9W47%2BlaVYHeUPOU1rCZtZ8U94r%2Fh0ASnyJ8wkx63rOTfBZUIH7EBnB3zJACDgWcEPCweFAPyJbtmzGcHZV6deILdqqfLCn9qDwVYKQJgPbocEAA%2B7hdQGwNJoJ%2FNn1c8dPfwaJBLlhculLBVFRqMNY2xokmwEHdnwXlB4CgrTmfqQKXVNw3WdPk%2FokIz0xngsMmxU1JeaOTG8mhxD7IysQowbyH624dbC2AEqxqfhjITiBeDDZgI69BjqkAWqmPXf%2BViPKB%2FjU%2Ffl9m0TN2WFkgxI0wMqc0AsxtvW5GV4mHocSENvK44fSHlo5C8Fehwc5R0T6BPiFjw50qI8M10imwVSa0khMbbMExWRx8dTPI%2FC%2FbxI38PEf%2FnUqf4xJdEExKrYhaT5M71rbLz2BATmaRO3LtYBrL%2FCvBB%2B%2Bc8V%2FQDG6%2FhVuCFex3Bq%2FjTA1cqR0jCL6VDBUdf9j64m4Q0%2F2&X-Amz-Signature=397f1c37d7ee95a7a8469d38114b0dc7eb2e0e9bc2700aabb4496a70c46872be&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPSS3RPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCOSDGiq0TKwFIaeXRqGNn3juQ9Ni3Rn9co2OLNyuvbYgIhAOYiPkPokXIniW6gw9KMtc8nMUEVSmA8jZFRK%2BFfiPkyKv8DCEgQABoMNjM3NDIzMTgzODA1IgyzsxysGbFog8CaeiYq3AMlxDIUYeNfCpk%2B0IWLDJd5OWw5rAXaFKWS6xEeq1qReMv%2F2eeUudoDrMGOy7xmiIGjDw9610aMo%2FFZKfj8TQ27f5zehxDg4fprupGiy2bmq8HkGTCSbsy7o8nOGpzo3C%2B4kMsaIIqBT2f9oU7cOs%2BHU94DSm6CsZMwdB3YW%2B%2FmHe1i4yCWwYHiEmvzEYmRCKCyjGaJYMhe6qYkKykqeEsbjm5kxLea01drLIVmXx3MDV33UEA3HAuaIJqXUl%2BehNQ7UkbyoJhHU%2BhQ5v4%2BHw9F1XhJq4jjlNYH6B6lDp%2FyIpUa3HabVYGtU69zQFAsG8BbQJu1q1%2Fiv%2BGLFS5QZQV%2BwWboLViKnvydN%2FH35LqXbeEVOSJ0cGa3GAOM06UQfbKl4n4JuJscLX9W47%2BlaVYHeUPOU1rCZtZ8U94r%2Fh0ASnyJ8wkx63rOTfBZUIH7EBnB3zJACDgWcEPCweFAPyJbtmzGcHZV6deILdqqfLCn9qDwVYKQJgPbocEAA%2B7hdQGwNJoJ%2FNn1c8dPfwaJBLlhculLBVFRqMNY2xokmwEHdnwXlB4CgrTmfqQKXVNw3WdPk%2FokIz0xngsMmxU1JeaOTG8mhxD7IysQowbyH624dbC2AEqxqfhjITiBeDDZgI69BjqkAWqmPXf%2BViPKB%2FjU%2Ffl9m0TN2WFkgxI0wMqc0AsxtvW5GV4mHocSENvK44fSHlo5C8Fehwc5R0T6BPiFjw50qI8M10imwVSa0khMbbMExWRx8dTPI%2FC%2FbxI38PEf%2FnUqf4xJdEExKrYhaT5M71rbLz2BATmaRO3LtYBrL%2FCvBB%2B%2Bc8V%2FQDG6%2FhVuCFex3Bq%2FjTA1cqR0jCL6VDBUdf9j64m4Q0%2F2&X-Amz-Signature=abfd9dcc8d788eaa9d9916ac826ef0a5cb014d9f35fdedb69a93daf9cb7b9d7e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPSS3RPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCOSDGiq0TKwFIaeXRqGNn3juQ9Ni3Rn9co2OLNyuvbYgIhAOYiPkPokXIniW6gw9KMtc8nMUEVSmA8jZFRK%2BFfiPkyKv8DCEgQABoMNjM3NDIzMTgzODA1IgyzsxysGbFog8CaeiYq3AMlxDIUYeNfCpk%2B0IWLDJd5OWw5rAXaFKWS6xEeq1qReMv%2F2eeUudoDrMGOy7xmiIGjDw9610aMo%2FFZKfj8TQ27f5zehxDg4fprupGiy2bmq8HkGTCSbsy7o8nOGpzo3C%2B4kMsaIIqBT2f9oU7cOs%2BHU94DSm6CsZMwdB3YW%2B%2FmHe1i4yCWwYHiEmvzEYmRCKCyjGaJYMhe6qYkKykqeEsbjm5kxLea01drLIVmXx3MDV33UEA3HAuaIJqXUl%2BehNQ7UkbyoJhHU%2BhQ5v4%2BHw9F1XhJq4jjlNYH6B6lDp%2FyIpUa3HabVYGtU69zQFAsG8BbQJu1q1%2Fiv%2BGLFS5QZQV%2BwWboLViKnvydN%2FH35LqXbeEVOSJ0cGa3GAOM06UQfbKl4n4JuJscLX9W47%2BlaVYHeUPOU1rCZtZ8U94r%2Fh0ASnyJ8wkx63rOTfBZUIH7EBnB3zJACDgWcEPCweFAPyJbtmzGcHZV6deILdqqfLCn9qDwVYKQJgPbocEAA%2B7hdQGwNJoJ%2FNn1c8dPfwaJBLlhculLBVFRqMNY2xokmwEHdnwXlB4CgrTmfqQKXVNw3WdPk%2FokIz0xngsMmxU1JeaOTG8mhxD7IysQowbyH624dbC2AEqxqfhjITiBeDDZgI69BjqkAWqmPXf%2BViPKB%2FjU%2Ffl9m0TN2WFkgxI0wMqc0AsxtvW5GV4mHocSENvK44fSHlo5C8Fehwc5R0T6BPiFjw50qI8M10imwVSa0khMbbMExWRx8dTPI%2FC%2FbxI38PEf%2FnUqf4xJdEExKrYhaT5M71rbLz2BATmaRO3LtYBrL%2FCvBB%2B%2Bc8V%2FQDG6%2FhVuCFex3Bq%2FjTA1cqR0jCL6VDBUdf9j64m4Q0%2F2&X-Amz-Signature=09af79c085c81527e4ca7c73bcb11f6014ca33d4fb697a7d5f47f024f1169caf&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=cdceb400729f393eb1a9df897bca25f8706724a7d2c060e7d2d9d58d7fd1c3d0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=5fb5871dd7dff9331d28a4d8f68018462dd049cabb9f93d5cc57f59735bab14e&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=abca09d7b8e8f1f031d5ec63ce926d591f8b327c1ee34f065e25acf32bceb7c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=1ea1aaf16207acb945a170369dc1347ad948e0537f4e583b2269b96011483a8c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=52ffbe5bc0c6e4ca5e0a449aa0cab36b9fd7f687f2964c942a22ee2d1924225e&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDH2ZDDB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDVHpKdijfEyyUYYqhDsP3TFTqUk28PI6KpumGlcJekJwIgPpS0gxs5GlHRBnuttc5Y%2By7iPGVQdbsskQ0h1qQiq6sq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDBV%2F9S2%2BsP5hbWX3CircA70xfFFQyZvEUMxwD4QDaPaPXEIPzes7tJaN961xVseeesy37jdq9yw6swutlmzpeRSIPq9SaqQ461nJSsIfkOaxR3XsJvA3mKfyY81%2FwiyDhD1HLs4Nst2LTiZoDz9yyqtgvR1O%2Fvdo31XxCJjRAd%2F0iSF4U0icsxmAne0lX11T1bAG60YjXCHo7QJcO%2FDrUfbfEa%2Bv7LRaDqTCTsvZhBlQpvUZEiNFuSTj1ZZF6jMmswniLvWfN3zvj%2BVXeHd9T2Fq3FoWlbh0NfbA%2Fv8bwxNQ71C8INKsLuTi0LWn6sSJ37GO8qsTmW%2FxvBEe8SyBIkBKWnpAeJm83%2FzPU%2F3reiYawb7Ypl8Fw744oYrXT5yzSL9iJVb8OTLm5e9NaLEKCFAXaZexTqWIiBE%2ByTRcb8zKhQwShGBkYKs8IageCw6FUdSXbHExDCcSMuiTUhHmGOKAWeNMbDGtXqVHnkaJCOL2Ol1t5qlUYZLvhnhDgTNwnc7iFbYzhOh%2BEjs0fNnOLVkB0e%2FcI4NpzcO0TDi07z6TL2rTHEYZrFtFEE9ObkcZz9%2F%2Fkl9eYlt5bv03Mv%2BWPK05JIQlC3BqwVl2svzwshQiU7lFNpXDLUvcMtLoPMNrW7xSxuY4d9fDLS%2FDMMmdjr0GOqUBQkMwPd0XWsDosY%2FMngEVOBH9XhkyGwJ5f8ppZUhrc9NxDL1ymf1PGai%2FFeFDUqIDRnqM1dJalC9SoDrfs%2BIDZwgZmokvGK8iH02hH%2F1l1ARRgbYpGdGqKcI1Y9G%2BQny7VQE4M5vDI%2BTqUxmRJBXkUUAbJIBQEVdnQ%2B%2BXNr1SYcvpAKr%2FG4Psu5Q%2B5VRS03LUTtiMmz%2Fi2y%2BcprFSU9rEvFELBN%2BS&X-Amz-Signature=fef8787b787845731daaad34d1ae55dbc2868248caec04e8c02796ff65d6b4fe&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S6TGFER%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIBOvzt%2FVEfhUkuawhkJcbYvYHALkB9V6FHP9tHvJz5m3AiEAov6fVoz2Va4vIONizB9EPO3sTlUIessJzIz2YfSdchsq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDOeTyn8cBR%2BOZOy5YCrcA352TOqWZdJypEX%2FRmBKW8Htuo54UcmDBhJtXy1v9ccTMb00VaQUlNXh4ccG2iAo1DnsLsQEjbh%2BEx9iKoh0UUqdTXYYc20z%2FvPfjNsbBXbKcn80T1V5G1JqTXjQAC9cjHZ2iVEiTmj0LdER8JjimqybGR6%2F4iTEO%2Bf9SHpegsOt%2FwyLXFmjY1e%2F4REg1S7ybs9zE6V%2FUJhlZLNjO1duKHFAAl9a9Lb95sYQUGGdy1gLMbPLvTi5sfdQsWuV%2BVSKB2nQA2MhBYZVHjZx3OBOGjZPRy%2FBIN%2FY4j8jTiByWGoXv55QkVPVE%2B%2BIc0Aw5F9b8cUFdqnwIiFOmpsa8sAkbS758ETpDiwhFhLQqer8m%2BvkSTvfLWElQnrcqyZqSFXn1DHa1EpM270eEklBGRgG1r0Gau8%2FOD4V4IP3W0rOU%2B0aWPB8TLT%2FhM61j1yOmyOWzkAYaMhvxVVS6uTkwcdwjQNzXjzQ1Gn5v%2BdQp%2BmJd1Va%2BTuqGw8WuzkjyYLSxRoHvBLnRqp3SGLent4iPBa%2F0MKVflNwrRSKP9tWC1TPpVBLUsIBJz0igCWpTjSXMg2jqMnKI1QbPPUv72P5Tk7CaD7bOFIA%2Bqg91%2BP%2FkcE5YZKt9zt1ZjUGPHBPYglUMNyAjr0GOqUBOrdbknXjt2fAaAFpQA1D6dQmfqnOHGJXnNpHqTXYpju4Up7C5wn5CdB%2BPdsLJIsMEhBHvQsFaL9XcTQbvUa7XIjQ0Kr8TMsIihnk1xe%2FTYdtTiyBOC6XnuzcsAdMuDodO6Tlkz%2FRC8jvbcuZ6yPaqP%2FYYsn8FrrmBiPXMeCOdrZTAeOO7xHEcNKc6gX7Yi9syzfmXzOq%2Bgxl4Ks3avPngq5XTC%2Bk&X-Amz-Signature=7edfec829637a392f7841b3828d165c811e70745b24279960e2652590059873d&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S6TGFER%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIBOvzt%2FVEfhUkuawhkJcbYvYHALkB9V6FHP9tHvJz5m3AiEAov6fVoz2Va4vIONizB9EPO3sTlUIessJzIz2YfSdchsq%2FwMISBAAGgw2Mzc0MjMxODM4MDUiDOeTyn8cBR%2BOZOy5YCrcA352TOqWZdJypEX%2FRmBKW8Htuo54UcmDBhJtXy1v9ccTMb00VaQUlNXh4ccG2iAo1DnsLsQEjbh%2BEx9iKoh0UUqdTXYYc20z%2FvPfjNsbBXbKcn80T1V5G1JqTXjQAC9cjHZ2iVEiTmj0LdER8JjimqybGR6%2F4iTEO%2Bf9SHpegsOt%2FwyLXFmjY1e%2F4REg1S7ybs9zE6V%2FUJhlZLNjO1duKHFAAl9a9Lb95sYQUGGdy1gLMbPLvTi5sfdQsWuV%2BVSKB2nQA2MhBYZVHjZx3OBOGjZPRy%2FBIN%2FY4j8jTiByWGoXv55QkVPVE%2B%2BIc0Aw5F9b8cUFdqnwIiFOmpsa8sAkbS758ETpDiwhFhLQqer8m%2BvkSTvfLWElQnrcqyZqSFXn1DHa1EpM270eEklBGRgG1r0Gau8%2FOD4V4IP3W0rOU%2B0aWPB8TLT%2FhM61j1yOmyOWzkAYaMhvxVVS6uTkwcdwjQNzXjzQ1Gn5v%2BdQp%2BmJd1Va%2BTuqGw8WuzkjyYLSxRoHvBLnRqp3SGLent4iPBa%2F0MKVflNwrRSKP9tWC1TPpVBLUsIBJz0igCWpTjSXMg2jqMnKI1QbPPUv72P5Tk7CaD7bOFIA%2Bqg91%2BP%2FkcE5YZKt9zt1ZjUGPHBPYglUMNyAjr0GOqUBOrdbknXjt2fAaAFpQA1D6dQmfqnOHGJXnNpHqTXYpju4Up7C5wn5CdB%2BPdsLJIsMEhBHvQsFaL9XcTQbvUa7XIjQ0Kr8TMsIihnk1xe%2FTYdtTiyBOC6XnuzcsAdMuDodO6Tlkz%2FRC8jvbcuZ6yPaqP%2FYYsn8FrrmBiPXMeCOdrZTAeOO7xHEcNKc6gX7Yi9syzfmXzOq%2Bgxl4Ks3avPngq5XTC%2Bk&X-Amz-Signature=09fbbfc5fd6a570940829b1cef4f5753751bea6e26f90be1b0339b4679360d66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKAB7C2Y%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIHteKBrLDCzu5C8umUd3KVoIjDHKA7%2FFcKx77pEuD8Z%2FAiBRKBTnwJ8qsvTBrkgVh9vRJcshuXKajyGe3Qv6jBjCPCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMi2ZsZ6%2BW89p3%2BZHpKtwD9Wo%2FMA11dfkLdV%2Bh1qZN0CZsX1jD1%2FxTNxMJVy%2FME4FEUH%2F54imdlMPUeEezG0gTLLEB6OfGG0pUcLDsNyYmdIkGCl0hwdvQoBxcrTTas5%2BiaEOxN%2FG2TMWwSqb0Z0E3QrDYILCGZo5Tve8VfBieEuhdtdHH9MMvrm4DcTMvgjPkQv9yUk6Xt5lXWva98LRJYNvS6hOMCSTTZZTJkW06ecHuRLorQ1YwRZ2Vew3F8dp7yEsMH%2BNXZ6aPl7fUbYnfwV78UXobBQzbdPTd3ztBbQxGgkJn6%2BATUyU%2F25HgjXI1OVXDBUpyvaLMzn%2FHADCM5EmAVYLMvTrGxrr09qQMvumo796TLQ0wI4EYgGjwLzmKUhVd681XcO0%2BwABHcmKR0olJluVcVtTIxMl4RmMwBtrjbTM4d8VkxPUjKevr8Et4wTOHSCx7vc6IAGCJ%2BZedJjECbtREE66GFWGmbLlQWMDO3gE8JN0ZCsMQ3qNcih9k8R14g0m3%2BH1Vs61SwhYQX7EUzv9H6FdNl8QPqdGyPKmK1uNY2rluydZugaJZDWWumLZvZBqmYn7liRV4olHX%2BkJ2MHEZspBm92Tr17IvliljPNVJXWSp21kF0JIb61D%2FeErfNL9xxtVv3TUwsZ2OvQY6pgHNgdPVhvwroefzWXSsxGkI6deKGAKsOqsw8P%2FfKPFSWIQXiNHTjR6Nz%2BUa0XV9KjcdsWtKN0fVFxA7AxRpaZLvcWtyWTjnJEhAc3G8M2tQ7R6uQFeWAX4%2BPWvNbs4YoAypMlYZNp0zr7J0w0LLPJIFL%2FewieiNQFoisTj0aEZ5mAyOMuhwcR5Bas46bOiAeKRIAfCX4k52ALodRCokaL8WAmOTOadP&X-Amz-Signature=84ff975c615a25f826c7817248d274bd14d6c148375f09a3a1e3d74f65907bd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X7TZO2D%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQD8rkAqUlkYsS9w1kaalDMDECZj2kGGC7M0UlVngnexiwIhAK9%2B9nEoD4KnXUD0sdkUBWyFoadVZOQj3FgWKLapVK5YKv8DCEkQABoMNjM3NDIzMTgzODA1IgyLhOn2rt5Vk8YTgG8q3AOTFjc43Ocd90fs8Gq9P0qt2h15f2M3fTgfpK%2FPeXfG8MNtP2HU4tUXWU%2B%2BRZaTglA4NCY%2Fn5di2dr26OkjdFqlAtdoBBPtSIiHrKqGyCuoVrvLptuZhSmGBlCe%2BA9wKxePnKANzAxDua94qZTeBCo8lzraPO3OYRvWJSIUyZQ6%2BUfW6FIb%2B1yCIt2hMPcaChjnwKZTmrKVEzhg0SRJLfna4mTtZ3YH3nubi9Yv7hX7NwcNwzCvAlKMyzF61aHXYDLArxxXZ%2F8o%2BvzR0FBxSq%2F%2Fu4ZGDi%2B0pgm7TH5guhtwqaKT2Xg%2BoluLpEXx1VpTsZ3U4q7Z%2FzfrEedjPpBb0NZhBll%2BERfUhZTcQ3fL4mXE3SGu6MWV1M4aviRv64S1I%2B2SPYEWugl7o3GPyFHN6rNjqsg2rxTUvaCMzgc5c4xs4E9HK4c7JlL24xgoCD%2Bt9zOQkDj%2BmFEHWRdqircB85re080pdLB7LI7MV7EXAu49wbHM7UOY8PoGhB1cMdkqTW3g1MwsHehvbLjZeMfBlXVHcNDDI9BMdBe%2Faz3XApRjrVOHYOB8W1S5Y9Msd8ZMgW5u8YD4WyB65ZT%2BemjxIC7BoGfin5%2B116hwnt4NtUVZV%2BRhL4EQpOCCQi%2B8qDDDnY69BjqkAUk4Wo%2BepTXCHMO%2FMkR5L95mXAeXBlE1UbSK7NWKpBmH9zj0jo1vxS7SCt3foXB6d%2B744X6%2FM%2FHhyhVhNktU%2ByE3xpSKyjKLR%2Fu6MU0zYPA7gQiHIRos3ZGpxEph2JMQq8a7KNvGz0wb7FOjVcOJ%2BVCGrLG%2FBnClWdC3Hl4Or2KPFzppajSDa7oj8T02d7eMX1oTeiAV4BRBBrqNNNYkeW0ElWMU&X-Amz-Signature=734695d642a7b38b5dd52aa7648b9e269a6c205e0500a8bb6d04e930ddffe5eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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