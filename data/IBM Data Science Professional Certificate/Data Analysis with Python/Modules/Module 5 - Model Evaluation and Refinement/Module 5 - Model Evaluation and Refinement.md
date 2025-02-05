

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=9e559bb656210190dbe13126bd3468f9860f0dde738a5fd09eacc3d8d0a6036a&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=dfad2851fad749c3a728944b023f2ab14e8c62cd73d9de0bc939fd969572d024&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=48904d58717426027ad87ad938befa275d5a6129157ee1ef5883787d002dadfa&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=8ab783cbef2f8f8d56973cbbeb9b1023e927904809b310e4b0803a16df2e4679&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=09f731e0cc4c58a68622f3af374a839c01c129d7ee057da70663955f0f9496a9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=69328aa49355bebcc744ddb6cd7b2c4146421772140f80e6555f9f8fb8bdf453&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=79fd3c3d3a174a12af556773537d9ccd678c9b0558646216354a8c1d61c156ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=89832b5cf4e02dbd3acc09ca72b0a979a2161021003587bb720a64ffa5f006ba&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=37ce7ff5c87aac6ead6633ec9bca0ab22e87c4750ca028925a5ac3e75deac4aa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV6KRZP5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC0rF5fcrPzzofBW4VelMP00w9sHxKU9lFTmSZkFZI56wIgdlZ%2BULVWv9hxZGyeeSn9hzsohOC6%2F%2Bvy3lQLc1Q%2Bmscq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKfVk7VQyWxxh%2BD1sircA8uTAaL1HBTNAeSOOMUWWOyWZQpdV99vHGpjD8DaqtULLCWjv1uRENQ11EHcc8uuAsVQDqdEo9uy9i4uVT6pExjxxcRmMLp6CNvtPuHR3%2FHWl6%2Fan0HD1oAvJssPtC9e%2B6deGt9g4C9pf7rXQYlrG6W2W0UN9AtI9W6AtIVNRx%2BF%2Bk21UuIZGQz6iyewsCgUzcOW8PLggcbu%2BfEyDWu%2B%2BJRLstrtrEMOdO1F02Zi9MMYwrPaZhRbB1bfukw2%2BK89M52IxucddVLJjBmNtmyywSvg6QorAIGxyeRrtezT6Pl2ch51pL%2FRIse9WlPHkjzvk7JkS0QPnrBRtgNpBZT1Q6j3YdpAq9z9BmoYPDuTC9%2FvutbxAVPjDiahjs7dPLrj3v%2FCkBICl7hEHcx6Q6kJyxU8QkmdWaSM26U352Al1adU%2FERq8XHtenaKu%2B4qsMliBKzBCjoSIOn3kRIdFoAyaiWWjwQO2bJkXHXzWDmNqtg%2Fj8JONyyzuYGGeVEtaNjyQtUlbg%2F4fa2haevHMaN5MZKx9PH4xFHRcfUs1H1B2Q%2F1YQpf0IZ%2FrfSkTxTEUq6Qdd3G%2BSyOO5fNfglG9wR7rVAUzM4dKkqa070bIa8NpVdPeavt2bIM2z0ip4gUMN%2BKjb0GOqUBF9NQ11zGfrSjncUAbEZPaMcHFDbbDsdx5SNSPoxrUjv1VBHIu1K6yhUxwOHyBfOZAx90NvYETNYHtaLPI%2FnN2sY4sHS3VnIpaPx8KNwZOzRiOUR%2FtV0oe2IwDVGIsqj85rYJlplRO78wveBOkV0kf2IXdGsqy60mOxt4A%2BwPwSmw5es2EqrCXb1KYupjf94b6mBA%2FDpHvcfEUIdHXpxpTDCGHCdq&X-Amz-Signature=0f2da9b2abe3de0cca7495f4549be560c703b446086853e5ce55fe8c1849a511&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV6KRZP5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC0rF5fcrPzzofBW4VelMP00w9sHxKU9lFTmSZkFZI56wIgdlZ%2BULVWv9hxZGyeeSn9hzsohOC6%2F%2Bvy3lQLc1Q%2Bmscq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKfVk7VQyWxxh%2BD1sircA8uTAaL1HBTNAeSOOMUWWOyWZQpdV99vHGpjD8DaqtULLCWjv1uRENQ11EHcc8uuAsVQDqdEo9uy9i4uVT6pExjxxcRmMLp6CNvtPuHR3%2FHWl6%2Fan0HD1oAvJssPtC9e%2B6deGt9g4C9pf7rXQYlrG6W2W0UN9AtI9W6AtIVNRx%2BF%2Bk21UuIZGQz6iyewsCgUzcOW8PLggcbu%2BfEyDWu%2B%2BJRLstrtrEMOdO1F02Zi9MMYwrPaZhRbB1bfukw2%2BK89M52IxucddVLJjBmNtmyywSvg6QorAIGxyeRrtezT6Pl2ch51pL%2FRIse9WlPHkjzvk7JkS0QPnrBRtgNpBZT1Q6j3YdpAq9z9BmoYPDuTC9%2FvutbxAVPjDiahjs7dPLrj3v%2FCkBICl7hEHcx6Q6kJyxU8QkmdWaSM26U352Al1adU%2FERq8XHtenaKu%2B4qsMliBKzBCjoSIOn3kRIdFoAyaiWWjwQO2bJkXHXzWDmNqtg%2Fj8JONyyzuYGGeVEtaNjyQtUlbg%2F4fa2haevHMaN5MZKx9PH4xFHRcfUs1H1B2Q%2F1YQpf0IZ%2FrfSkTxTEUq6Qdd3G%2BSyOO5fNfglG9wR7rVAUzM4dKkqa070bIa8NpVdPeavt2bIM2z0ip4gUMN%2BKjb0GOqUBF9NQ11zGfrSjncUAbEZPaMcHFDbbDsdx5SNSPoxrUjv1VBHIu1K6yhUxwOHyBfOZAx90NvYETNYHtaLPI%2FnN2sY4sHS3VnIpaPx8KNwZOzRiOUR%2FtV0oe2IwDVGIsqj85rYJlplRO78wveBOkV0kf2IXdGsqy60mOxt4A%2BwPwSmw5es2EqrCXb1KYupjf94b6mBA%2FDpHvcfEUIdHXpxpTDCGHCdq&X-Amz-Signature=b7ce59499469262bce4b3549ddbd8dd88d1eab321f7321730a98cc5815ea5339&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TV6KRZP5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQC0rF5fcrPzzofBW4VelMP00w9sHxKU9lFTmSZkFZI56wIgdlZ%2BULVWv9hxZGyeeSn9hzsohOC6%2F%2Bvy3lQLc1Q%2Bmscq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKfVk7VQyWxxh%2BD1sircA8uTAaL1HBTNAeSOOMUWWOyWZQpdV99vHGpjD8DaqtULLCWjv1uRENQ11EHcc8uuAsVQDqdEo9uy9i4uVT6pExjxxcRmMLp6CNvtPuHR3%2FHWl6%2Fan0HD1oAvJssPtC9e%2B6deGt9g4C9pf7rXQYlrG6W2W0UN9AtI9W6AtIVNRx%2BF%2Bk21UuIZGQz6iyewsCgUzcOW8PLggcbu%2BfEyDWu%2B%2BJRLstrtrEMOdO1F02Zi9MMYwrPaZhRbB1bfukw2%2BK89M52IxucddVLJjBmNtmyywSvg6QorAIGxyeRrtezT6Pl2ch51pL%2FRIse9WlPHkjzvk7JkS0QPnrBRtgNpBZT1Q6j3YdpAq9z9BmoYPDuTC9%2FvutbxAVPjDiahjs7dPLrj3v%2FCkBICl7hEHcx6Q6kJyxU8QkmdWaSM26U352Al1adU%2FERq8XHtenaKu%2B4qsMliBKzBCjoSIOn3kRIdFoAyaiWWjwQO2bJkXHXzWDmNqtg%2Fj8JONyyzuYGGeVEtaNjyQtUlbg%2F4fa2haevHMaN5MZKx9PH4xFHRcfUs1H1B2Q%2F1YQpf0IZ%2FrfSkTxTEUq6Qdd3G%2BSyOO5fNfglG9wR7rVAUzM4dKkqa070bIa8NpVdPeavt2bIM2z0ip4gUMN%2BKjb0GOqUBF9NQ11zGfrSjncUAbEZPaMcHFDbbDsdx5SNSPoxrUjv1VBHIu1K6yhUxwOHyBfOZAx90NvYETNYHtaLPI%2FnN2sY4sHS3VnIpaPx8KNwZOzRiOUR%2FtV0oe2IwDVGIsqj85rYJlplRO78wveBOkV0kf2IXdGsqy60mOxt4A%2BwPwSmw5es2EqrCXb1KYupjf94b6mBA%2FDpHvcfEUIdHXpxpTDCGHCdq&X-Amz-Signature=023d8033b9ebb29258a22c9675d3bfbbd04df6fd05c3531b9b9f9f3e818a0c9e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=eed010eb02d8da4a722d8a5e08bc173e704a5f7e53ca523befb002eb91c5cd8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=626de2926868d22ae5b7417cb9e658a0c873851a1b40b8de7b3d54ce3521aa32&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=b5eedac6a8c2ae422706f4b982f4747dc44d55ee4f51b6356934b8cf7e014721&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=2a33357f200014ae08ee678c1b9f2f81f7e27d2aa30904214208033ddd995ece&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=1ad4c223b8e17a344e269854efc16f91b4aad1df697b10bfc86d7d0ef2c99520&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YAI2IAA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIHm9ed5zvVlS7LugiD9qn6jbhyDCjvE7PMYi0FuKhq3wAiBNIN1ZjFRUrmhkBeZ0EvNm%2BwFIqmzFZrot%2FQgZujxCWCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM9HjUIXmjSqIYQlS8KtwDM39ej%2FpQXhwJiEW%2BXgYKWV8HDQRUTSKD37Bl0h%2FbCGwG%2FlMG5khlh7hBf6l0nsbwqclxhNi3U1MRkOoqlJ%2BTPLRhkogBczUAJBF50vu6qkMVatWayNHfjcjVqABJTizmPBP59CSIvaU%2Ba8C7jWUUUkUsVH7mEYRm89P2EHIC%2BMkVXNxqHmp8hsjQ8CqSuv%2Fu4leUSALRAPjDs9mIRJdjHItQxz%2FNiDECpTUyqvqmZG1dPwA52fhUxn1uODGBjWOaMt4%2BP%2BYDOcQwDCiE9ahbhurxClqRGMlc%2FtEInrvKokf2XJ1q7yHf%2BqPbRBD%2FsJP5%2FAatX8k8eq3GuiNaq%2F6pDKVF2c7La1F4YkyhUUTJXLDtCiBJMhLKJHy%2BkQEO7xdMntwfesMF4M9ARIrUujbhY4s4MKSQByOmpMEdPtTB5452ysGBX%2FMFDfCywNwQwhzJhGjzhNxUeEtxaPiM2H2Lz27eLTqMl69ocRLvnGZEwLdGJWA%2BlKyGCDg4yIeur%2FpBl%2FM4AoWr7%2F52ciAWuWwsBHzhtv1gxWSq%2By1mcOUCOeZX%2FHTomIRwRpg%2F6jH%2F4WUADvTRaFJkBOSm9RkzVH3K2RO0iBDBw0IEXtM%2B%2FPGxXVvr%2BPs6bZ%2BjiCbXhjswnYuNvQY6pgG5PwBs86v%2FSj442H2yOh7z%2FnbiSSuVCoOFqkoyABQHFApe%2Bh2EFHlevQJ%2FJ2%2BwNp24una8E5gCHx%2FoPr8pBxYduZRPrRUifP32M7Muzti1ZRKwjAkrImEChw37ZMi6hejSS9Tjv2jUusefurSYKXmnrvB5Dv15dpawF8K7d66LVMWKxJbW2nHBvTJoXNQzZ%2B04aufnK973dff%2Bv0UkJL1RaZnbQRV2&X-Amz-Signature=653d3e59e17d1f07dfc7b2d186d1b277fabaa7b66bb7fbb73c802eb5a4e49657&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP2TCMMJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIFi4mUV%2Boks54mwgR62XZp6ceY%2BZZc6zKpmsClQ%2F7ao4AiAsoNMsuoXpq%2Fti%2Frzmn3pxhBl3L81dBRBlkODCjGHlWCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMuYhEAe2BFiejZWQCKtwDc%2Brvi%2BiCc7ixkZHOeBijHOhJGtnSx6lw10Ur%2ButMcxSMyako4iVwLEqRgBODJ%2Bezui7m1W%2F2EPVzMuCi4WXRt8gtHvLbhY340a3I7dDZNrrFmP%2FasGuFsG2HfyP5hWlWm%2BJXoXuhXFHuso0529yh2EP%2B%2B1GTbF8NlluqiKmrb7SV8mnaTlwUgBU3DsebYJvn9%2BmqKHb335QyaO1fhY2ZZgWdzGuUiJW0jPNmimqXOmD3KMMiUDA5%2F1Yl2DvEIBuKJOtjplfsyIRe%2Fq5nnC0HDJDKwQ0WbINPn%2BfuIlVS1DDb1VznkmXUM%2B3sMIPKZUE1K5cXC1P9x9VOJoqQO6ETtxXH8iI2TNMxR4VqUMLwZDmJS03%2FmqqsRkAqwxIjM8rkR7%2B8oshZfZtQr8x2vXC7tzi2agnqsrABeQhjlbEAkLY5Kr%2BAKfV8RASvhFSuIQQaywfhHeR%2Bkct015q9FWay%2FRhFxLOrP%2FyI223m7WSM%2Fvfw5iv79yKGEhpdyVLWhg6Wh3Nun8bQVm%2F1mRn1K2psG%2FTUpMqzjKLB5KVaKxcqMN9JygRv5pLmugeEAK%2BK6zZAzpyl9vslykLH1CxFHxFiLix5Lt9n58RX6vVoC%2Ba%2BCqfXV2Yls8iWiR2QwCMwgIyNvQY6pgEM9TBIRtJSYT31892pt4EUov4CFU%2FJsfi19dfWQOZixQ%2Fv1fyu9UDxSiLBaB%2BNRvIIBuO4FXnb9Tywc2V%2Fw2x9zX%2Bxfr13QbNRLTCod5prFVpvKL3LDPDN55SihHWY7odiTcYIX8pXsUqEMe6MbvLjBjvUZkwY4j8fh2wNwRP8G%2BPc7xDzX5%2BPebP8f3c6VpLEwNY7Nz2uFa7C0FlRQ%2BB41eX%2FFPmx&X-Amz-Signature=bf8171c243e1eba2a907f70efdc8a4b2f52f06fd1da1bda670ab2debe8b7e455&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP2TCMMJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIFi4mUV%2Boks54mwgR62XZp6ceY%2BZZc6zKpmsClQ%2F7ao4AiAsoNMsuoXpq%2Fti%2Frzmn3pxhBl3L81dBRBlkODCjGHlWCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMuYhEAe2BFiejZWQCKtwDc%2Brvi%2BiCc7ixkZHOeBijHOhJGtnSx6lw10Ur%2ButMcxSMyako4iVwLEqRgBODJ%2Bezui7m1W%2F2EPVzMuCi4WXRt8gtHvLbhY340a3I7dDZNrrFmP%2FasGuFsG2HfyP5hWlWm%2BJXoXuhXFHuso0529yh2EP%2B%2B1GTbF8NlluqiKmrb7SV8mnaTlwUgBU3DsebYJvn9%2BmqKHb335QyaO1fhY2ZZgWdzGuUiJW0jPNmimqXOmD3KMMiUDA5%2F1Yl2DvEIBuKJOtjplfsyIRe%2Fq5nnC0HDJDKwQ0WbINPn%2BfuIlVS1DDb1VznkmXUM%2B3sMIPKZUE1K5cXC1P9x9VOJoqQO6ETtxXH8iI2TNMxR4VqUMLwZDmJS03%2FmqqsRkAqwxIjM8rkR7%2B8oshZfZtQr8x2vXC7tzi2agnqsrABeQhjlbEAkLY5Kr%2BAKfV8RASvhFSuIQQaywfhHeR%2Bkct015q9FWay%2FRhFxLOrP%2FyI223m7WSM%2Fvfw5iv79yKGEhpdyVLWhg6Wh3Nun8bQVm%2F1mRn1K2psG%2FTUpMqzjKLB5KVaKxcqMN9JygRv5pLmugeEAK%2BK6zZAzpyl9vslykLH1CxFHxFiLix5Lt9n58RX6vVoC%2Ba%2BCqfXV2Yls8iWiR2QwCMwgIyNvQY6pgEM9TBIRtJSYT31892pt4EUov4CFU%2FJsfi19dfWQOZixQ%2Fv1fyu9UDxSiLBaB%2BNRvIIBuO4FXnb9Tywc2V%2Fw2x9zX%2Bxfr13QbNRLTCod5prFVpvKL3LDPDN55SihHWY7odiTcYIX8pXsUqEMe6MbvLjBjvUZkwY4j8fh2wNwRP8G%2BPc7xDzX5%2BPebP8f3c6VpLEwNY7Nz2uFa7C0FlRQ%2BB41eX%2FFPmx&X-Amz-Signature=0bd90434b5e921a639a21062745ed1484b137f9116f6ea1a19a1f1102b93f65b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE4EXO7K%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCt%2F%2FdQk2rHhpPrRiBNbcYyj9sM2wnvDlvLWun0GPXv8wIhAMlFkh%2B4njBGJ5Wsmfd7P7juOSBKYPCgyep1HDz5HkqxKv8DCEQQABoMNjM3NDIzMTgzODA1IgxZC7g2ArUtyYN8w28q3APD5HZ%2Fxtb4mjunDLDzglq0xghAjTXRei0RxfjfxpSqpp0zplIE9uHeUz2JTHifspeL9maG81VhPnJLvX%2FxDD40cFYwktJfxvb%2FuYamfTfDa5M%2BiJekmPMs3quKIcdCyBxe%2BvSiEuVNki1oBHrMcEhoEZXheAfncNz8wdGxPxCiotT3N1hneu%2BMrxSleGHdgGMJjRegCeJrKe%2FgHnDRyAGaomEpjHX7HoZI2vLQoT3jh2VK%2BegLUV7v%2Fgn8XdKAostYIBD0khmng0ZWNR9hOHQPUYl3KweUmBognXZBL4KceWsBT6CTuLU9dlvL%2FG58Im6X34%2B5pOei2OULJ5pwysw4rwDYE7F0JdUYs8KDcgU%2FETWm3LZUzYFALM3qVqfpl1VK6Y9p%2BRPnKRjhEDeO59DHnnq5yPdhUETdA3TXvkOMMqg0Y9EmNpjg8e0FS28BS3cXK%2BEIwdd33pugM7Y7eCgeliqWnfLzMhS1QQ7Rc07NWLqlk5St8pJgqbnmAowpavL3U9rv5Ta9htscnhheNxaTxYowevh7b5YlOWWsqYST3xLYaZYR6AF%2FSdaA2ZCf07%2Fu%2BgZpU3lVBQuFlK4MfSgOPDJKCFJcT3SpW7dhcnc5h7au8S1rotXRAHTNlTCRi429BjqkAda6TTbK6laLP8FpzALrBxUWaCbpMLcVhqAurS2Dc7%2B2iGnEecNlDgaXFlFXek74nLSChynWBVw2nOLvqRaNolxqbR7HmU00CX6g3IQM%2FXYZf8eqGoMQ%2BANuSNa4aDCpGIKg%2F%2Ba%2Bal6FApBUuqs4MHqnRIEcWtq8o%2BC1nNU02XdUR79XhGiLw9vpefIz8dwTZTCSeZQ8Uf4BP%2FvQEqeBdnStQGVO&X-Amz-Signature=509964112d400699bffed5d2cfc9f9a3c0ae64b8f74ed22a990f8bbd3dc887c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQLELPT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T122948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDgVFadav1aJh3eTvqDbKwKSNexKi5nLdU94R6vaF6gwQIgJC7f2N5a8sdOqJ%2FaH3tTyJmOFZoIzUii3Hb6t7cxs3oq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO%2BV1nOlqIO6e%2FzNMSrcA%2FvjYUcwCJTWg0Ke9o1c3Ec853DBkj6Kg6DPnwEgoA6%2FttRVqMjsaKvARwvFWdKicGFJZpLCHy9ngIT05D76Wtd9CGjoB%2B4sokp7xk66CHmIsqRrUrYz7Zesq8xLXqkwfNT5K2skfjswXxUI%2F3igEHjDgst9w5V55Cjom45hnSCVKvOucobuEB6bBWY3kT%2FTNZyYUhYOJzmSvCnfgJnnsmDWvP%2FB7X2QlXaF9HrIhKiF3GQOoswzt8oFmcDGfs4VhH8DglzRVuRTK5yBmHgfvrnlwZ7tAjnf0djxhQtIqK00RuHUXk1MxBuwF1F%2BdpA3pv%2Fag0UtJ1a53hSioSW3nvhOskLX9Q3ZhyJ%2Bz%2BkKkrWYv3PwEcgHYyFN0e7LPYsqHBvp4FPkONB%2FQsWv%2BMcA4yVVk%2BYTJBXX7c0lLEFry30LjJIzpMKCI8hmZKK%2BNxzVNQjIKhVYZ5m9gW4rcgsztJE3j2nBhdbHKdY5hp8zZIgGBlaCAjnwFDDBHIvsUFLIEysHfyEwLCDIg7EDfVbqmGcTQ9OhQxyyBZsdSJmAmk%2BxdvymmPc3PF06AqVP405rfBmnODHdqur2QFaovNGeMaf8UZEyfoA6LDF%2BZkbE%2FSMmQPOgCRty0gW%2BJlS3MOeKjb0GOqUBe4NkgeAURmEjt52KrwLOHZ1UiLzQ0Xrm5YO4EZboQVAeqKZOzT8hA0GqI8MKmCGahkxBaDM1uhKHq2GgLzAgFCR2udX47cuk24nres3X8Fw2K5WxQmElxetR8M%2FnPc5yA5XA1tTmwdha3CTly1veyTZkcGTYCAm4%2BMgHgnE%2F17v%2BZ5ksd32jp6gVWP28vcK7ptmIzmXKK04qxmq5g2NakWib9VEp&X-Amz-Signature=96995559e501c547780c312e1780e437c959d57305d6941c185a09426c41ded2&X-Amz-SignedHeaders=host&x-id=GetObject)
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