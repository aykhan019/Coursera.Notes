

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=56b6bbbbbf89e5826b56f7b7dcee78b2163c4aaca70d1121d8c5420ba545c1fb&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=60564d1d1c6cb0dc63b21c43706ce318e536c4eaa00e9136b907adca45a31386&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=d6cb0fb99cb79ce83bef8a970d35458e43c7b214548985aa920fa2d031dfb630&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=9f5280931b2a3d04603ba26167a785002d4273160dafea45feb2e982fb741efe&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=686cc92be5a19be8762d4c105d9a59a361115b3b1928a9864b6040f689fb9e0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=36753da11d0ce43f4dfdb3a2c7a8656ea236f335b2089780cdb9b534d907659b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=acfdb147a80fed4e35a6ac8f605ae4e533c1c7512e32ada79d23dcd872d3f6a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=88d5522e63d3bb8dd55107df40ff6bc7735ad99e544fefeb3bcd8b567bd2172b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=02a9670749170c37323d434bf258b0e5776f7ec3ef2a651a8193909f032433b1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TLVR3HF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDdSczrFWW6UKgdpX7iXEkX2oIHHslz%2Bt5cu2TpbhO9hAIhAL6eUT5njbQJ7IqQLl6wj6lghj4TM0dyO7v2D6gXnmXSKv8DCCkQABoMNjM3NDIzMTgzODA1IgxCUWh2kRKsf95cYCkq3AOspNKBcWDJEofPO3pKp3kKi2rc1r97sGhMXD68OVYKDhTpftcDmTET2xI4if4RXSOVuHYsbQkff0Pup55M9chX7glfovLCBcYqgiHIkRMe1Ih7hlKyw8mfEzqKSJX5knEbRJj0oJmAt3cE8OJru2xxmp91URwiAshYYtdHL7yDhA6h%2FlPDEH5BmuXTt8uJcRWqpqo1EvHchYmbMo3bA%2F0BRnGMzHnvhRZ2u%2BXUCNS3MYrzJHUZ0A01EUmF9tq5DGofFnWojFciWbkIPTi%2FbeR%2FSu6%2FhhJHvJRCY1Iva5D8QWjVbItHOapms7StC8MBdoqF%2BHZ%2FZt11dNqkx0w6NHdC2zQ7OBd6wliCMMdOkqehMSEgzWfbNsZJe8eaqLd6m5Lwyj1xQAb1TZ%2FC6IDaJPmE40niSxk1SvCAl1iFhkmtcujEV96R1R3t5ArQfWh3QKOegMs10NPdCF5xXMGWgY9Z80nyJit1khC60%2FAGzAdArQMZeP7p7Pq3NxJugupMarZSEwvIOiI9f3GDBfTd0MzdeDdrxY08sAhfkAWrPLwqMCDMjB2qoj5PX2suaOKTBjdvC%2BiAQ0jCcnr9I0%2FmxbQYdugZg7EiwIP2MF83qQrAYqxM%2FKo05fVAhDZ1pzDTkYe9BjqkAaX368NEB8IYsFSWOjU%2BXHZVjB3q2AkqfOh9Mn3Jyc5qSYLk1fLPncF1zqVlx4RlUHmQvbj0qiCGYV2tsdtEwQBc3YYmvYMVn%2BvoV6C5iYS1LLHI1L91nLxx9VqlveE4zcTJMBkZa8Srlgcu01cr8BMgC4tTj7G6VI5D3C%2BAtt2ikYiSvGs1YeLZa3YSlD5hffFVKYJyqUODRlIxKc7kgMw9h%2BeF&X-Amz-Signature=3a18f7b52224af4e02966218a375e3cc32c9ad110aee859e5e79891fc92d43d5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TLVR3HF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDdSczrFWW6UKgdpX7iXEkX2oIHHslz%2Bt5cu2TpbhO9hAIhAL6eUT5njbQJ7IqQLl6wj6lghj4TM0dyO7v2D6gXnmXSKv8DCCkQABoMNjM3NDIzMTgzODA1IgxCUWh2kRKsf95cYCkq3AOspNKBcWDJEofPO3pKp3kKi2rc1r97sGhMXD68OVYKDhTpftcDmTET2xI4if4RXSOVuHYsbQkff0Pup55M9chX7glfovLCBcYqgiHIkRMe1Ih7hlKyw8mfEzqKSJX5knEbRJj0oJmAt3cE8OJru2xxmp91URwiAshYYtdHL7yDhA6h%2FlPDEH5BmuXTt8uJcRWqpqo1EvHchYmbMo3bA%2F0BRnGMzHnvhRZ2u%2BXUCNS3MYrzJHUZ0A01EUmF9tq5DGofFnWojFciWbkIPTi%2FbeR%2FSu6%2FhhJHvJRCY1Iva5D8QWjVbItHOapms7StC8MBdoqF%2BHZ%2FZt11dNqkx0w6NHdC2zQ7OBd6wliCMMdOkqehMSEgzWfbNsZJe8eaqLd6m5Lwyj1xQAb1TZ%2FC6IDaJPmE40niSxk1SvCAl1iFhkmtcujEV96R1R3t5ArQfWh3QKOegMs10NPdCF5xXMGWgY9Z80nyJit1khC60%2FAGzAdArQMZeP7p7Pq3NxJugupMarZSEwvIOiI9f3GDBfTd0MzdeDdrxY08sAhfkAWrPLwqMCDMjB2qoj5PX2suaOKTBjdvC%2BiAQ0jCcnr9I0%2FmxbQYdugZg7EiwIP2MF83qQrAYqxM%2FKo05fVAhDZ1pzDTkYe9BjqkAaX368NEB8IYsFSWOjU%2BXHZVjB3q2AkqfOh9Mn3Jyc5qSYLk1fLPncF1zqVlx4RlUHmQvbj0qiCGYV2tsdtEwQBc3YYmvYMVn%2BvoV6C5iYS1LLHI1L91nLxx9VqlveE4zcTJMBkZa8Srlgcu01cr8BMgC4tTj7G6VI5D3C%2BAtt2ikYiSvGs1YeLZa3YSlD5hffFVKYJyqUODRlIxKc7kgMw9h%2BeF&X-Amz-Signature=93a6c333d0d5b20a0b6344f90112a358ba3525f5c6e5d91b326bebd58e8143da&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TLVR3HF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQDdSczrFWW6UKgdpX7iXEkX2oIHHslz%2Bt5cu2TpbhO9hAIhAL6eUT5njbQJ7IqQLl6wj6lghj4TM0dyO7v2D6gXnmXSKv8DCCkQABoMNjM3NDIzMTgzODA1IgxCUWh2kRKsf95cYCkq3AOspNKBcWDJEofPO3pKp3kKi2rc1r97sGhMXD68OVYKDhTpftcDmTET2xI4if4RXSOVuHYsbQkff0Pup55M9chX7glfovLCBcYqgiHIkRMe1Ih7hlKyw8mfEzqKSJX5knEbRJj0oJmAt3cE8OJru2xxmp91URwiAshYYtdHL7yDhA6h%2FlPDEH5BmuXTt8uJcRWqpqo1EvHchYmbMo3bA%2F0BRnGMzHnvhRZ2u%2BXUCNS3MYrzJHUZ0A01EUmF9tq5DGofFnWojFciWbkIPTi%2FbeR%2FSu6%2FhhJHvJRCY1Iva5D8QWjVbItHOapms7StC8MBdoqF%2BHZ%2FZt11dNqkx0w6NHdC2zQ7OBd6wliCMMdOkqehMSEgzWfbNsZJe8eaqLd6m5Lwyj1xQAb1TZ%2FC6IDaJPmE40niSxk1SvCAl1iFhkmtcujEV96R1R3t5ArQfWh3QKOegMs10NPdCF5xXMGWgY9Z80nyJit1khC60%2FAGzAdArQMZeP7p7Pq3NxJugupMarZSEwvIOiI9f3GDBfTd0MzdeDdrxY08sAhfkAWrPLwqMCDMjB2qoj5PX2suaOKTBjdvC%2BiAQ0jCcnr9I0%2FmxbQYdugZg7EiwIP2MF83qQrAYqxM%2FKo05fVAhDZ1pzDTkYe9BjqkAaX368NEB8IYsFSWOjU%2BXHZVjB3q2AkqfOh9Mn3Jyc5qSYLk1fLPncF1zqVlx4RlUHmQvbj0qiCGYV2tsdtEwQBc3YYmvYMVn%2BvoV6C5iYS1LLHI1L91nLxx9VqlveE4zcTJMBkZa8Srlgcu01cr8BMgC4tTj7G6VI5D3C%2BAtt2ikYiSvGs1YeLZa3YSlD5hffFVKYJyqUODRlIxKc7kgMw9h%2BeF&X-Amz-Signature=078747cd6a6a970fc5de2c83caa4a84c4874ea8b85f458247d870a2ce3e02299&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=4aa9c8fe6fd18bb03990fc28a257d8ec2195f6fc944daa25e16045a876391e4c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=c174a00de67e967931be709dc4e9c28157ba5c8d47d4d3dfeb95a01db3d717f0&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=167ab1e2d38ed1162e9c5760afdcf7b3965c7242c5ec21a0161e7570eeb86f60&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=9c5f83dd213f57dbf4cded7aa088b6f6459fca7a6a40d6e8a5f175be9215a502&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=7301fdba2df28b9f824587959bbb3eeeefc9cb04932a7825b4b02c76dd1a6571&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SBHQKSR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIH1T1k1wKXHiv1inb8u7CwmAprB70okO3xOP0DkN3T59AiEA%2Fnharz7SQh0SLVLwZcY4i5vVbcmB%2Fbh09HC7YDJ00d8q%2FwMIKRAAGgw2Mzc0MjMxODM4MDUiDG3GxFLsxLcrrRx%2FzyrcA0%2FDePCLLDz8KCvVsF1M30dxCWYAbkDMtcsrWG709OUup9QkAbxlaqM7iojC6xsEoj5174QsZRx2jZmi7x6sQ7icgzX%2F7NqlIArxQQrd62bkReLh%2BfbsveGtX888p5hds1gX00Hf%2FmHy7TCWGoHK3UtMlgzRclwjk0uoqJmDMPcz1JIdIyiWd5OAnwonKhLjl%2BmShsi5OD5aX8JvchCxsbel5CkhgcqYFEz6NDx54tKY%2Fek5WidOmldSQN9%2BElegyz9hex%2F1NSdezrJBSAFwHrw8wf%2Bpq8a1kmjt0u%2FkERtzeRlGMI4jFoKtxBQ5OeOnjZE4E0lL1Gl8hmKKOMCcgYH6fr1y5pEtiucP%2BXa6yKkTqYx8XoNzraJb5qN%2F4OCsEk6lbjZT%2B8Re%2FdStYZjAlQot4s3isTWwSpJfNikwfMKXv240w0Zp6VM6WEYn7NVQSY9UVgGIWZGRSeW4SB5UcUZ8QrhmGwyrdRERfvKfufeBG9OUtYrUptYMeoxSU%2BUh5bFdpt8BGtVNTfLOk%2F5%2BX%2Fd8iV2iOTSO7vsktQQqJyKrODvB%2Fk1U%2FTIfvaSJFhdarMJYn8uOyWVaDFxJ5oZvVKVvDuRlDAC54zIoMqfeMcpeSUNmBSWf4NKoEt3xMJmRh70GOqUBErwb7m7hqblOOKnxpzvhF%2BxpGk6TouOhQL0Buj%2BGQwtCtxbVGXyqwZKwzZu95kSrEaCmZUS0WhTMzMeG3SQwApMq6CbjttQNXi5Texc4sEgNcT9MrMe0ZAdMAOG7i5m3GFD82XWgzYHzLJTLRBkZcf9iRPRP1P5TUmm2RL1AKjFD0o3C9GpRl0Hj7gQgXMF2yV7ppBJEWJ2vGAr7dYgwZCmemcB9&X-Amz-Signature=d62563dcc888d9a7b57caa1a88b74faec787f61f420df96ebd9b4678e3c3c532&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4DNWDET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBfog%2FunT%2FFIAEacZWko6BkJMBqC0cWzsRwaJVbwuabHAiBDEh4uVywR9w9KVfLLYtNG4L46tqwinmdvvaXtl%2Fas1yr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMqQ7qQHAYcQ0b5QUMKtwDorNPMBvNwr5RWgK2WvFhYJPtjenXQ2oEdT8My1tF8GT3aO0zc%2BLxJwx1zCfmoVmstdvX%2BY%2FrA1uwmU%2BUHV00AOzaqQotsx%2Bz00yATRUr3%2BMP2Row3%2FDezChOsdFfeFbRfIf0iXZBplAOkEm6dNJRe%2BDkkQFXpYa6u5xBYfsnQYbnE%2FCh%2BA5YBuKI0D95%2B71Lr3%2F9XYLCuONuZMSlsZVZ%2B0zNP%2B1B%2FVQhTolYamYTNwJ0sjMbjqs8XnG4H%2FWiCzvcRW0L7ZV0rgWvLSYY6vgU2w%2B8ZN0pTwm24KyS%2FBnL%2Fe13J84PURuNcti8zEggsD57xFO%2FR6yvKHmJ7r2Lw3DUbs7ws42ZjUvUZDGmluLddq0%2BUJrqrOZpodfp%2F0geTp6yQmsnXsbdAm77JdiQLsgpR24UMlAdhAunhxvQzPAh%2Frs%2Fr7D0xrJhadttDVtIDBlWeE2wz4TgjyhVUUvt2j14Z2i6sYeav40yJ%2Bnz7b4Oac2EijRvhV9OV%2Fiahxg2gwQWm7w4tfcbpX7uwIfXroS8BauaYRuJSr2mdIKRgGm88AtfKVRjwagFnheTuldc0mIyQOxmnnUuMZy8R1tOgc12x1YLoC%2FLDCcB7VdeseD51CHKn7YpfkmQG9nfMHIw%2FpGHvQY6pgG2JKfSbfddxJDePHX6Qu8x2YbT4VFA7EN1KRugW%2FF4M2iJrHPamo99CLCse%2BjYbEgLt23Nd0%2BRHklzWHQ3tXGNmAAwfli3HNz2vVJeUG%2FMQig1nAtPNlGy5ELSPS6V1PkFuYsFl04BuoTi9IijJKdeJDefbgS%2FYguK%2FYUVr5RsHYboY5hapunKL48Q72oxnMo07lN3FQxMs4ZNOt7Vsna3%2BqINXfMm&X-Amz-Signature=a08f792aeb434d9fbe242e81909c1899b67f257d9aa159022a1ecd6a3b3b1080&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4DNWDET%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBfog%2FunT%2FFIAEacZWko6BkJMBqC0cWzsRwaJVbwuabHAiBDEh4uVywR9w9KVfLLYtNG4L46tqwinmdvvaXtl%2Fas1yr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMqQ7qQHAYcQ0b5QUMKtwDorNPMBvNwr5RWgK2WvFhYJPtjenXQ2oEdT8My1tF8GT3aO0zc%2BLxJwx1zCfmoVmstdvX%2BY%2FrA1uwmU%2BUHV00AOzaqQotsx%2Bz00yATRUr3%2BMP2Row3%2FDezChOsdFfeFbRfIf0iXZBplAOkEm6dNJRe%2BDkkQFXpYa6u5xBYfsnQYbnE%2FCh%2BA5YBuKI0D95%2B71Lr3%2F9XYLCuONuZMSlsZVZ%2B0zNP%2B1B%2FVQhTolYamYTNwJ0sjMbjqs8XnG4H%2FWiCzvcRW0L7ZV0rgWvLSYY6vgU2w%2B8ZN0pTwm24KyS%2FBnL%2Fe13J84PURuNcti8zEggsD57xFO%2FR6yvKHmJ7r2Lw3DUbs7ws42ZjUvUZDGmluLddq0%2BUJrqrOZpodfp%2F0geTp6yQmsnXsbdAm77JdiQLsgpR24UMlAdhAunhxvQzPAh%2Frs%2Fr7D0xrJhadttDVtIDBlWeE2wz4TgjyhVUUvt2j14Z2i6sYeav40yJ%2Bnz7b4Oac2EijRvhV9OV%2Fiahxg2gwQWm7w4tfcbpX7uwIfXroS8BauaYRuJSr2mdIKRgGm88AtfKVRjwagFnheTuldc0mIyQOxmnnUuMZy8R1tOgc12x1YLoC%2FLDCcB7VdeseD51CHKn7YpfkmQG9nfMHIw%2FpGHvQY6pgG2JKfSbfddxJDePHX6Qu8x2YbT4VFA7EN1KRugW%2FF4M2iJrHPamo99CLCse%2BjYbEgLt23Nd0%2BRHklzWHQ3tXGNmAAwfli3HNz2vVJeUG%2FMQig1nAtPNlGy5ELSPS6V1PkFuYsFl04BuoTi9IijJKdeJDefbgS%2FYguK%2FYUVr5RsHYboY5hapunKL48Q72oxnMo07lN3FQxMs4ZNOt7Vsna3%2BqINXfMm&X-Amz-Signature=623bd3949d10af46cb5388bbaa979515f8cc08053fa8720f393ebb8ceae948c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AFUDPDF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIBecjcUlxCW%2FNER8f9eqXpvyMORpFKdFh3WXg%2FHuGeSdAiBdvOUDLMoc4aQzmwDE55NTqZCGUrH7x6HH0eOvoa6wCSr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMBCEhUsBglRI5EINXKtwDYOz4kP%2FmRLEEyNqecOz0mjxYQnH2Jvc06eL6P1kBEsPPCZvYgatdnfxyF7kpW%2FeKu02fdNPx58F19BALIRN%2Be%2FMuryvnduof5e%2FQQ0rgn6m2jJ6YqRT5QPBPiYY%2B3sW14LcHiPiQLrVV5gYOzmjFe1tBzMAxUP6d4mImcOcJ%2B2Bh9om%2F1une2NXMi0QVMGyhRs8jfH7%2FEnbfLp%2FQWBnM9IqfSALyHFnPpNpMmaeiSowSqFPPFee1ODy%2F9F9Ipz04GBkBHeM7n1PHSHbBwxJCmhfRSrQBcqJD43PKHI%2BPtmDDJMQWz2nZ%2Fo%2B8UG9QKrg%2BvCa%2FB%2BraUsdCKz0Ozmc0ZhNi2mYmhQ8l%2F%2BgVOJHEIcJQ9bg2o1AXU6u3gZw8QkF%2BKghULqhqWCQGQCszVcAKdJdhul74K5jNDffdvnjE8NzGQT1Cw9m%2Bjc4HAmQvQjIc24QWsq9NaySU3CTn0i%2FgZq%2BgcfpssT%2FKhPNsK4aPu9zvAPjbzGB2WD7Bh9W5zvOeGoHSC%2BZj9iFMaJAPsTnwtbaoSzruM%2FlzYHYq%2F6bkzANP9t%2Fww%2B9bUu1KKvVMfiFhZGxsxUDrUdDC3qnExSBsHR7m%2BhP%2BMSnuNMlFsai0CguhFwwDTSfSbNMIhFgw%2BJGHvQY6pgHSQjISuF54zizSZk%2B1GrmjJUkG744x%2FvshDOhxTn6YNRxzonIrSYSBPwzibNLnDfHTls9dtQqjAWaeTclrUq7JAKzdEaXvD7oqjBsup%2B3GUdzREnsww22ZY6BOLHChAkCGCESbaz9hNEvuVRHpxma9BnlJ0K7%2FezU2rQaG9FM6h1Sv55hCYP3bcqaET4vtdSl%2BY0M8iYsr0IPy7Y%2FaSMMr7m4309pU&X-Amz-Signature=d15d5bc4501e0f391cd30de6e8abe56aaf22cbf46d3d08b36e1a4b624638974c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H6FQC3O%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T081912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQD9lI4VzWd%2Brw%2FXu%2B7DlShK3yqW6%2BBUU%2FT1rZ6cvfar%2FgIhAP52n7q5C91lVM5dnsk0KO9w2AnK2sHgo504HBFutP5MKv8DCCkQABoMNjM3NDIzMTgzODA1IgwmS3jjs7T1tN8NmiAq3APEXUJuzl4T%2Fgb7WJtRQhp9LhE2A5eauftU5%2FSTNr%2Fky31nICHuEjum9BTUKRq3bZQNzJpkMIZUWMWJV5WyTBh%2BUdjEjNkcePStQMNmPwWmWvbPB4BeeYRtnuNbIHTpAQRlr8%2ByZoCidzbW8DaBZ73YvITqNxEr46%2Bd4m8PpPW0DPTwCp3fyTOx1kmh%2FGp%2FhYNM%2BR8WTnEp07VNfu2hAhe4h3bDM6SE0M1PAU%2FjClLs9rfD6hVbR4lhlz1uMj3x5HeOJmwbN0s%2FJcG7ZOmNmL9RP4bDCyctqQ3%2FR3wUVVEf7DHm5dW7LdeEyBRJ3BVA0u3c7Hykd3td9PsDaNudbzZkuEpIjVtGHTuA6PDZwSC3M6%2FQtTZfGn7vyqRxOf%2BnvI1lqtsEuARrXf1DLv2qiLwwNg7V1BLzpW4v6W5EHrfDOYOQZDktMFhVCq7yHW5KRpIxfgF4mRa%2FfB%2FOb%2Bs1QVIs69wDqgVpVLtHNjmyPBcrF79nxOO5zk4VWCZZ7Ul984F4Uywz7Lhsb7f8f2Qvz4vWG2YWEjBlNBSrWP1ULfdMYYB2t33YZxlrMavXN2XR%2FWckyWVuWNlaaWF8xwnDk9Uiml1iHD%2Fdtxx9Q1VC7BG4Yv5whybL4Bz%2FRXIYlDDwkYe9BjqkAcCF252CdTPdp%2Fcz5p%2BjkrCijkDi5Eun%2Ftiuji1BTFQCwVnuwP0EHyr64V1pa2ImkxYCjhw2zV1w8%2FT9%2BoKSgp1HaBWigCFiZKljWkNmgzzWHpNt7RmSy2nKrm%2FUT5B6Z7ETq5byoPow6kryitPvd72z%2FB2LCUB2Ix%2F342sWz3NGSSS44QmKMaJVYm4SMpE4Zn8eKXYns4kynrm5Zt3DjnmBk3DB&X-Amz-Signature=98fcd27335ef46e19a26a52d345aeb6258049898b7203e5bdbaf583a61c5f45c&X-Amz-SignedHeaders=host&x-id=GetObject)
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