

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=c4ffb2ca6c8f4e3a377c68bbbd6126bc62733b3b697c010d2708b72d469f2fc4&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=9be86a024a116e57c245332f61a6479b85be51302e8acbec5b6e25424f474a21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=480a3198bf23d92263230cc49f65db63238ed7b07cf71d3e0dc1888dd7e02c04&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=d96ff85e1ee2dbd58c8c3115e1c6e03e30f69a2c8c56f80af4f057464421e37f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=da746b4ceaebd9b71a38d395e2c76f76830430e8a353b2276f51ba104bbece6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=226788d18d13c2ca85b606f27479093869b025e0dcbca966e9854adfed387e47&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=7c80aa4c98460f48fdecb9666cb0803f26c052d54334b4d04a6820769fb9ea72&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=3a9a604612ebdd54a9254ce14116547e0faeecb115193424e6230abd23636cca&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=339cf5a7440bba7d8c1a29a84681b81f9fe89be92e9e4e3380818780f487eb6f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUU7ROCQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCJUwjMBZeAci2RyjXAPprk7kKYh6uGqexGPV1usZn0VAIganMQ7YVbOiIuU9zV%2FPiPYP8iGt65AP8Fy%2BgNSWwFms4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC3cuSoLpFOgyejL5SrcAzOQP4wj074iDZDpqO1Fx7C2t79nskid3riqHPXvVWGeBw5zky5P5nLKP8aJ9yqfabj4siveEZGJeOfvaoaeU5iX3Ik6MDI5809tp%2Fq2vKRGwPUCY7w4D5Akg5itEY2oyBVOQmGP9er5L3w83g%2Fhgs%2BgNTGDlsM%2BmQl4dI77SunmywOyQJngHnQvSLobmifby2hNZ0NWUzBMIfqS1hwkUSJMMIoyCoDOFFhGWVdpTAwzRXDA0DdtervSksxNHtcW9O7PXOdZCpVIaUjCyC%2FTwSqnsjHOHUHBe%2BUCVt%2BsvZDJzxqxXFGA%2F1Oox5LaOcZJEjM9Ahd0gDylyfrblRchSU7TBhQYbJN36EJIP1cp%2FSXCqBPSh3FwjCIBqM96bfKJcBu%2FZ7nZWqXs%2BI7W03lIJ3y20bXXV%2FNiZEjxiHVCA2Z5aWePZ6a%2FNDiDYKW501FNlst0w0S9hTW60rm%2BZp3YFIx3dNt9CPBuzfPIFfzBraur6u5sP3cFtOL%2BVjOXCyY1wvyTPyLddRp%2BikKp9jxkA8bQOlTeIrB%2FTujf3W6ZfSwssR2Umvf%2B%2FN%2BZzgPLRhumqomolkJw%2Fkm%2BqVPN3liurFI%2BUdwUf1vjxLuFaxICXho3DsJ%2FKGG0ogNp5DeoMJno5bwGOqUBX8AHV20H%2FGKC8C%2BIMU%2B2bDtK0zWINwU1uY2G0n6ZWlzKF%2FbTAnwO7DC3HRLtyhKH988y2izrofhRw4LhCFLxDD7fsRH567I%2Fi2v0QDeGsTiM9yhVMmr91FjDYPb9ckI6Hwl56Yq8%2FlmD0ySjuxZTZKKpYaTaO8ng%2Fq1oWD1aJsPjuUzMzEUdLjkc%2B3u8hWnjnD0CdPQ4QOjkCdKYU35dv5CHUp9u&X-Amz-Signature=86b3a383e0ef6212bb6ada6aa2f9c4a4584e8628ed0012c00ec7965bd7c2364a&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUU7ROCQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCJUwjMBZeAci2RyjXAPprk7kKYh6uGqexGPV1usZn0VAIganMQ7YVbOiIuU9zV%2FPiPYP8iGt65AP8Fy%2BgNSWwFms4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC3cuSoLpFOgyejL5SrcAzOQP4wj074iDZDpqO1Fx7C2t79nskid3riqHPXvVWGeBw5zky5P5nLKP8aJ9yqfabj4siveEZGJeOfvaoaeU5iX3Ik6MDI5809tp%2Fq2vKRGwPUCY7w4D5Akg5itEY2oyBVOQmGP9er5L3w83g%2Fhgs%2BgNTGDlsM%2BmQl4dI77SunmywOyQJngHnQvSLobmifby2hNZ0NWUzBMIfqS1hwkUSJMMIoyCoDOFFhGWVdpTAwzRXDA0DdtervSksxNHtcW9O7PXOdZCpVIaUjCyC%2FTwSqnsjHOHUHBe%2BUCVt%2BsvZDJzxqxXFGA%2F1Oox5LaOcZJEjM9Ahd0gDylyfrblRchSU7TBhQYbJN36EJIP1cp%2FSXCqBPSh3FwjCIBqM96bfKJcBu%2FZ7nZWqXs%2BI7W03lIJ3y20bXXV%2FNiZEjxiHVCA2Z5aWePZ6a%2FNDiDYKW501FNlst0w0S9hTW60rm%2BZp3YFIx3dNt9CPBuzfPIFfzBraur6u5sP3cFtOL%2BVjOXCyY1wvyTPyLddRp%2BikKp9jxkA8bQOlTeIrB%2FTujf3W6ZfSwssR2Umvf%2B%2FN%2BZzgPLRhumqomolkJw%2Fkm%2BqVPN3liurFI%2BUdwUf1vjxLuFaxICXho3DsJ%2FKGG0ogNp5DeoMJno5bwGOqUBX8AHV20H%2FGKC8C%2BIMU%2B2bDtK0zWINwU1uY2G0n6ZWlzKF%2FbTAnwO7DC3HRLtyhKH988y2izrofhRw4LhCFLxDD7fsRH567I%2Fi2v0QDeGsTiM9yhVMmr91FjDYPb9ckI6Hwl56Yq8%2FlmD0ySjuxZTZKKpYaTaO8ng%2Fq1oWD1aJsPjuUzMzEUdLjkc%2B3u8hWnjnD0CdPQ4QOjkCdKYU35dv5CHUp9u&X-Amz-Signature=57b800179876fb508bb7f23c1281e2d5ccf834c49d78645f8baf0ea3833a7b6e&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUU7ROCQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQCJUwjMBZeAci2RyjXAPprk7kKYh6uGqexGPV1usZn0VAIganMQ7YVbOiIuU9zV%2FPiPYP8iGt65AP8Fy%2BgNSWwFms4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC3cuSoLpFOgyejL5SrcAzOQP4wj074iDZDpqO1Fx7C2t79nskid3riqHPXvVWGeBw5zky5P5nLKP8aJ9yqfabj4siveEZGJeOfvaoaeU5iX3Ik6MDI5809tp%2Fq2vKRGwPUCY7w4D5Akg5itEY2oyBVOQmGP9er5L3w83g%2Fhgs%2BgNTGDlsM%2BmQl4dI77SunmywOyQJngHnQvSLobmifby2hNZ0NWUzBMIfqS1hwkUSJMMIoyCoDOFFhGWVdpTAwzRXDA0DdtervSksxNHtcW9O7PXOdZCpVIaUjCyC%2FTwSqnsjHOHUHBe%2BUCVt%2BsvZDJzxqxXFGA%2F1Oox5LaOcZJEjM9Ahd0gDylyfrblRchSU7TBhQYbJN36EJIP1cp%2FSXCqBPSh3FwjCIBqM96bfKJcBu%2FZ7nZWqXs%2BI7W03lIJ3y20bXXV%2FNiZEjxiHVCA2Z5aWePZ6a%2FNDiDYKW501FNlst0w0S9hTW60rm%2BZp3YFIx3dNt9CPBuzfPIFfzBraur6u5sP3cFtOL%2BVjOXCyY1wvyTPyLddRp%2BikKp9jxkA8bQOlTeIrB%2FTujf3W6ZfSwssR2Umvf%2B%2FN%2BZzgPLRhumqomolkJw%2Fkm%2BqVPN3liurFI%2BUdwUf1vjxLuFaxICXho3DsJ%2FKGG0ogNp5DeoMJno5bwGOqUBX8AHV20H%2FGKC8C%2BIMU%2B2bDtK0zWINwU1uY2G0n6ZWlzKF%2FbTAnwO7DC3HRLtyhKH988y2izrofhRw4LhCFLxDD7fsRH567I%2Fi2v0QDeGsTiM9yhVMmr91FjDYPb9ckI6Hwl56Yq8%2FlmD0ySjuxZTZKKpYaTaO8ng%2Fq1oWD1aJsPjuUzMzEUdLjkc%2B3u8hWnjnD0CdPQ4QOjkCdKYU35dv5CHUp9u&X-Amz-Signature=0117f1a53f6463923c3a3a3fc315c6b69a5ed8c52850394eab11dcedb2103392&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=d0ddc7bbe77ff50930a7f0901da300e3b4975b6206043c2f1c3c54c2f1b867cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=25cf20597712b808591649f089a9a2338cd568ecfa6894c2145922eb4ab3f540&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=abe3f276701e7547930249ca920250e1b7a05de5b845ee2b444499b5a4106aca&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=e3ebba21ae416ad17cb710afc7b7bb72b85ccd885af36ac3fcfd8facf98256ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=193ad8446bd412856901a6931d475eb2768a34973e3b9998e52549f8b6342593&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663D2ZGMN3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIQC5QL3WaA8%2F%2Ff%2BdMp6%2FHUqsAHX4bnuRjPC4G0u67Gv5DwIgBjGfxO0Y23Z99Quf%2BrN9o0eVDso07wwsThzoMhM73hgqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKQ%2BFVqAoYjhf7MD3SrcAyK4LUgAy0XbcPJWSg2EnR118QziPzS7D6t6xckkQg30T6D309yF5iUojy6sSTL%2FQKjNRL5vrG9DBE1%2FGY7TaYWSg2pZzkPbWOQFSqIyIaB2i3DLwRG9gIKdcdGKuoX2rOwmK3tAAj3UbunCu75BrhtYFP9HOi1APObHe6OBh7SGEl%2BAtOwdb1a1MU3N%2FmgCSBd7pUK%2BfhNhFRU%2Fn2LQjKLAycKqzb7RDi8p%2FsgFbjnkqt%2F%2BdTi3mXbuWH9%2FmhXW1lb%2BTAUo%2Fk%2BNDWPT20%2BQT%2BMybdl0MxGOH3GaY%2FeQJLWqxZfb%2BckrtRRfRcNZczKdvVjkooSVSROizNzodF52XeH2d7Cxv201tqaBApIccEez%2F3fS0En6%2FMy2f4mpOs2mv5pKcgrP2bT0EbpDFhx2%2B6h9oqCuA6hyVC%2BVR06PrAM9uoi4OB8I9%2FviMu1EA%2BDjGBGLbst24PD85khY2KBKkXNR%2FC9vA3YeHTUGR1rX3PTmWsdK4s3EunuhLPQMqs0EdNvHYW0b%2B6zSmkfzHgQfU5TfXzoqK4wiBxakhXK3skyVjFy2lvIBNcsWbh62CbbR05ytZyfCqWWvEOHYSyL1Z4v%2BUW%2FmB8oLMiaREHPz9ImuOSAe1HGORwc9xtpxMOLn5bwGOqUBdj14SPlFtuPBZ1NhKC7V7G5bncBgU45X9Mesk6cT3inuEUVl%2FHOc5CvUEKil1Ve9UEynQ5QHo2vTDlfYtsoGmjs1cnfmVbTxBDWs8sLqlhRZxLjZ4f%2FCCoQYiY%2B5%2F5AGdYjGMyQCG%2F1K3wMCkjEPTtN2TcdIYqOwwB9xnoWfUG9RjoJB1UWUYinuTP9P747RmZ7ivs8xyowSc%2F%2F11FKsjBKb2d67&X-Amz-Signature=839de79cc373f2eee0de982aaf2d0e192ea35827dacfbc593c7216e8f891f8e5&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDAM7EH2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHboVlOvYqKTFD4hJfH43CMy3lRgEP0pDQB0iOudgJtdAiB8imuiKuTuKUQoEywAmA1ZGDvqQMK9%2BKKhp7fgwxvYACqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6ewn1SbGR%2F%2Fc7Cx2KtwDngl25VNoSUfv%2BV7bWcE1JzLDIAWkzm72DzVGWUoFtEuQekDf8thP57d6Z8nDKRiuLQOGDt2p88ErGlDqRqU3QhcHPA%2FKsKf6GOHZYto8GROifR9fEwXGji7OS4rt2fAEIdAfznV%2BzL1RMoV3EtC%2BrdHQqkqEvLaQI8f%2FXtqsqqp0AiFRIWLPy26Db%2FsQksZo2rtvYUNB7ovvZfHISu%2BzB1Hgv2yO4konmlEHyfJ0wkv3q%2FiHdXKfUeHsznCMpQXuK42XtlxTBAJVD5jEldV6rAvI4AUXqnfVDx0clEhGYzIa5XXG5xJ2PD6gDt0HfNXKEiLlUjCBIqHLQSml1YVGDa1K%2B9puEQgGlDWDMb9QenZFVKeQF5tKQpgWzZWaGDR6veKuPgk8Zsp5DXW6918jbxtUElzm8r%2BOMGytTWQv8%2BB%2FAH%2FPXATY%2BipYhDOdda6pLt0%2FO%2FYbAF6Kx6pev7MsNJTOP7218I21%2FabxCM67xjDCPWqkdgjAzKa6ya%2BiZPUUDtnK4tkiRRwq7c3pxjMPyxJRtQpwoUmb6tyqAoQjszWqRkmEPc9cGjiFOERPoI4fGRBCHtPSP7bFAFnDQ77zn4x0JpmB%2BkoQBsY8ZmxUgDviQGSXekdTyr0J5v4wmujlvAY6pgGKE6COy7SIoanTVQXq%2BCoa6ZsF2aUKlK7mzwJcpm1vxhCExxqyypqH08iQg2PnYLJ4It0Dsbkqjv5qXUA1zpzaLRjJexvb81JylpH9LVCDzj5f8zdwYDsdIRQkKa%2F%2BhW3NmQTO9dCcl0MoiR0N8VdWXAzpamrGA7D%2BVL1rC%2BXDHlxrmj7teLVlzuSQeNaPnl%2BuGA3byoY05IV8QVyqbmkkWmMlU8ay&X-Amz-Signature=1bf50aa81586e685da0f180a5aac2af4b1792fa6714bb96f89557b382d97777d&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDAM7EH2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHboVlOvYqKTFD4hJfH43CMy3lRgEP0pDQB0iOudgJtdAiB8imuiKuTuKUQoEywAmA1ZGDvqQMK9%2BKKhp7fgwxvYACqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6ewn1SbGR%2F%2Fc7Cx2KtwDngl25VNoSUfv%2BV7bWcE1JzLDIAWkzm72DzVGWUoFtEuQekDf8thP57d6Z8nDKRiuLQOGDt2p88ErGlDqRqU3QhcHPA%2FKsKf6GOHZYto8GROifR9fEwXGji7OS4rt2fAEIdAfznV%2BzL1RMoV3EtC%2BrdHQqkqEvLaQI8f%2FXtqsqqp0AiFRIWLPy26Db%2FsQksZo2rtvYUNB7ovvZfHISu%2BzB1Hgv2yO4konmlEHyfJ0wkv3q%2FiHdXKfUeHsznCMpQXuK42XtlxTBAJVD5jEldV6rAvI4AUXqnfVDx0clEhGYzIa5XXG5xJ2PD6gDt0HfNXKEiLlUjCBIqHLQSml1YVGDa1K%2B9puEQgGlDWDMb9QenZFVKeQF5tKQpgWzZWaGDR6veKuPgk8Zsp5DXW6918jbxtUElzm8r%2BOMGytTWQv8%2BB%2FAH%2FPXATY%2BipYhDOdda6pLt0%2FO%2FYbAF6Kx6pev7MsNJTOP7218I21%2FabxCM67xjDCPWqkdgjAzKa6ya%2BiZPUUDtnK4tkiRRwq7c3pxjMPyxJRtQpwoUmb6tyqAoQjszWqRkmEPc9cGjiFOERPoI4fGRBCHtPSP7bFAFnDQ77zn4x0JpmB%2BkoQBsY8ZmxUgDviQGSXekdTyr0J5v4wmujlvAY6pgGKE6COy7SIoanTVQXq%2BCoa6ZsF2aUKlK7mzwJcpm1vxhCExxqyypqH08iQg2PnYLJ4It0Dsbkqjv5qXUA1zpzaLRjJexvb81JylpH9LVCDzj5f8zdwYDsdIRQkKa%2F%2BhW3NmQTO9dCcl0MoiR0N8VdWXAzpamrGA7D%2BVL1rC%2BXDHlxrmj7teLVlzuSQeNaPnl%2BuGA3byoY05IV8QVyqbmkkWmMlU8ay&X-Amz-Signature=b8aad5d054799d30c7de8ab9e282c864f3c91d43da18908696ac29fde1b419de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDZG3SJW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQCnCM7udtENlKI4dL6TSfELU%2B9X0AnTVzYKfiGXU8tfcgIhAO5fuWDr7g5NMGHrQr%2F35mgI8ICoG8r297XPcbIGsV6uKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyK4tUDZUIk8L7Fa28q3APP7cW3lFPOwSfbPbiNPcwSXw7A8o74sLcjSydrLCazMepTJ4z3YuWDG3mQwpR86MadIrdDr5N7ps1zCOJR1fCDdaz1R%2BgJ2BWLMI6xzovtzvM4ytbsGRXNRQwlqrbql8idNX1L08X7qaLxdOHK2D4l%2F6twVSH3gpoifMVpaaOzoz8v9RpQlUPV96eNWq%2BwpRFgNRXJ4nYh4QAhCD%2F0QF0P1NEKqM9am8TLAaVbPeYKaSuo6U5HS2oQi3op9V8n9K3eJrV6UhkdqeBzp6suR2vtrWAeIWnXwiV8XQVJt3dogcvfeXsk9ESXBno1ZS8LAEt9ZW%2BK2Iz1TL5opZxcUa%2BVAQXr5EJxaCPM9D0ps360seRwR1kcEr5EFnjOSqcRzyKp8cwEGHP8aEx1zxEwJaMJcCq1Z0O6wX2dSgbVkiPWN7caeYPdcc2OrdAlJx6WCkG6W9nZYGwRSBHKSe5UW2cfXaFgXDIQf8CAnILFeUOw5ZG%2Flh0h8kiX0%2Bx4SMcChuNLW5%2BFfHRVJfYF4WTBdsrR9TMqQ7OZyQYStetfn%2FMwhWewRv3WQMYGLV%2FlV%2Bu6nna2YGNCXvv%2FQsmCZqoDGoFmsjxg4NNBfiLn%2BD5b4qK2C2gcPZa3kTgv8kEEdDD%2B5%2BW8BjqkAbOPsyVk7Hrlkb0aYpNXpJHegfMyVsh0MSgZxXVmMg8H9BPpx%2Bwu5CuI7lova82IFtQj6EBg7EBAEDysULCaEuVfpNpdvGnKbkzZgSNSG0369pLrxW4yhUKfUNlUqCUnhJ1DNnBvYs3ZJyH5yCbD1zSegXip6LJjfblNp8EecWHpbcAIivJ7PFPgEb3TouX6oj0%2FdmGiUXIlIDk%2FJnewGqeivPI6&X-Amz-Signature=b0b0af6c9f7f236a652c96a79418950127d88ebc9ab616f97142bbe1b90ad80d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOZYQ7Y6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJGMEQCIHCqgmf7Lb8bkjHxK0YAuTM6aolFEtGc6U60hJfwBufWAiAEc7wx%2FQEFk4nHkfEVH6iKDr%2Ftab5durnCv%2FC3alOAtiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmFv8H59bVukjzaQ2KtwD5XpvzsfJB9OpAoJ7BnAVWzfVg5ue0oWrvlF130SfGS4V0VqtXa%2BWOXAfP%2FpUHvX0QDC0AUffBUOLGc6wl4M%2BAbTsJ9%2FiFrPZZQJj2a5YMoAEAsQGAro8OnvHmOLSVbqXlz1UH%2B%2BK%2Fxxacu%2B4wIjd9dsCYDWm%2BPIUuscofxpuf1TFuPooua3CsJsbrAgXwdR5nd%2BM0FPeRT6FBpuJyQcEgccv8LpIo3Z6WxnVBrw%2Bl4WRPRjIzl6LR73PUT%2FSZ5KmonhbDgEsd5ipa9iAl7b56CzqqdSIGWBUhidPHd8iP5KPqWdl%2FgfId%2BtNkJH8RIl1hiZSd%2BVJzgTUjDxraaGiWkKcX0NtBD3V22J6HsIJFO3gAzlPEAeddIQDgsXLV818Cu7D7TPN5TF3h5bZNYOvWyis8WgJha987kNHizI5xf1XqCCi1dXy3uesw3Gxyyi3LiNcQlclxUUF7JBYUH2ricrZ9OIjU7cKF9uVO%2F8WDO8oV90LU%2F28j9%2Bsnojei%2FsdDSH3VNBYuQDnK1wEjhpNICE8jRPPJQR5mPQMs0eB7rr3pQcWgp1a6mdMBujeVlua1WjNKglyBcH85iyrjn%2FoYjtTGA9UeNNRpeFNHHHtUkhlLC%2FCI22HcNKWbyww6uflvAY6pgFATGkovNwWugBQraE46F7qbqsmafryjCFitnAfhXpw7dIA20Si3D%2BV1rJKF0DWVvsJ7K7cI3oUXoXLU8WHZ%2FsYwu%2BNiAEr86E5tOKmFNtLpKwYhwGza3y81FKGhtKWAemTYJAV1oT0pk1a4sEKdtnHrGFyukWYW0ElihGsHukO8szddOarkp6EY8HPdibG0tfRyFynq18zq%2BFhe5ErMUut9ZstRdjC&X-Amz-Signature=ab159e905942c99dc988c7c63ca4eeb412ed097ed00934ef558affe770080476&X-Amz-SignedHeaders=host&x-id=GetObject)
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