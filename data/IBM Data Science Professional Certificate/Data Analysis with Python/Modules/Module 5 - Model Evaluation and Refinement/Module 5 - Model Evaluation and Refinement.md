

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=5d9554bbc278fbe311510a0383fa97c38dc357bb9f59163f993d8bf64d9addfa&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=d2f71cb273d1c70ecfcc6de53d91ed0cb1fbfd034b8a72397a5ab7ceb7be2583&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=e359e8f7e7a98caf8b2a4978fe8ec911fde97ae0d00da31f1616a24d0a4f6bca&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=33c153ac1e31962833342350499704ac9d0c471f583edfeccfc06397fdea9c2c&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=174ff61770f656ee305d7d043388316ff1280966869f9c139da9714dd78c1eec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=34f1f3eeb1b92791a6dbf46d7ded41d0c8db578c4c7b1dfd7e4ae415ba0ec836&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=3c04e9f97075937ed2a195fe4a3d6486b3802b78ac389993f39d09c8e5748328&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=395dd04214fe0e5d2cdc5baaa3513147a6a03a1bf518bbef66d5ca33c14111b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=62582879a3280db0c6153cdf166eaecf66e73632021c3fcb8ab7d1cded080f75&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652IKKQPQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA66tySQ0IYwO7%2FIi%2B9s65EIpa7mrXTGnSumNqVB1Y%2BFAiBFAGVt%2B%2FJdLleMTqurbqHOg8iMzQDAbicCklgOPHaEDiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vmP8ZvFhTv0xn3qKtwDz27YBxxN9Ck8LLniZ4mQGyR9qG0%2BmzvFl3vRVa%2B4POGDJtyOwdc0b1dl1j5Ht7RtIEeLGWImIbFnsY%2FVELpPLZMppLC%2FdUr%2F%2B7HwPDxMdqoQrvIjbrtC0h7rE4X1auOKdtyEqsTCcB%2FTRe6Ultp7CBJXNGR54N1cGMdeo7maKs5bavY1sq2eM4oF2kS14RmqB1ioGykxGnxwNKgAREKFOG3KNx52s%2FaViVY2hdJ6sao3gXpWAJ6VOcVgil0Z24hmO6jimuksxlthvaMB0tOoJR1c30VBWMITKeL6qp3DfJ6MouLIz8Jh3ciX1Rt7gXPQYnwI0nRTxxeennCh8sp1ZlG4gotKFwnzUgCG%2Fn41n0FYnicK2I%2BUxtLocMlKN1VYh%2B%2FVihYL%2FOFFy2unEgmEqSNIDncIk1cz%2BxZrkkuO9tAqLeksOGbqF1GUiRUvHmWMWDA9t8fri2nb5%2FQlrjHbP6ig6xM%2BiO1gAc4P%2B0CuPaoR0c%2FC6kxBRE%2B7Det%2BqTIPRGtdVDdmSdERTk8aRj09EBBjl15uUL3uXU%2FwyKrDgSRVRDJO3nUZ6PceeWkAxjn2rrULkI1tEd8wVzzU%2B9zUfBNT1t%2FOfKLaMcc4p61QLsMrvwt8NIwIHvH4%2BDowyIWdvQY6pgHumZMEHTYmHYfXL5aUNUZQr5GEaQpKVT8m8Ai55tz75vv2FYZPhTqCSGFpDMzTLsezUQIvrwzoB8Ulz8cQgC4h%2B4Enkl%2Brz0GITo2FTvUVvmhy%2BO520Owvx%2BFzPVAYUTQaerJ6uqDdVQOxf5qikyOtdOoaaig07KzAxxmGN90hRjspdxKLWn4cx5H6fEGnWbovPeE1TaZRj4cjrEmTumseO4k2YnDv&X-Amz-Signature=d7e5aef33af1ba8962a7c3da4a01237d7e8df6fb94257a8f5c91aa415b784dad&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652IKKQPQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA66tySQ0IYwO7%2FIi%2B9s65EIpa7mrXTGnSumNqVB1Y%2BFAiBFAGVt%2B%2FJdLleMTqurbqHOg8iMzQDAbicCklgOPHaEDiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vmP8ZvFhTv0xn3qKtwDz27YBxxN9Ck8LLniZ4mQGyR9qG0%2BmzvFl3vRVa%2B4POGDJtyOwdc0b1dl1j5Ht7RtIEeLGWImIbFnsY%2FVELpPLZMppLC%2FdUr%2F%2B7HwPDxMdqoQrvIjbrtC0h7rE4X1auOKdtyEqsTCcB%2FTRe6Ultp7CBJXNGR54N1cGMdeo7maKs5bavY1sq2eM4oF2kS14RmqB1ioGykxGnxwNKgAREKFOG3KNx52s%2FaViVY2hdJ6sao3gXpWAJ6VOcVgil0Z24hmO6jimuksxlthvaMB0tOoJR1c30VBWMITKeL6qp3DfJ6MouLIz8Jh3ciX1Rt7gXPQYnwI0nRTxxeennCh8sp1ZlG4gotKFwnzUgCG%2Fn41n0FYnicK2I%2BUxtLocMlKN1VYh%2B%2FVihYL%2FOFFy2unEgmEqSNIDncIk1cz%2BxZrkkuO9tAqLeksOGbqF1GUiRUvHmWMWDA9t8fri2nb5%2FQlrjHbP6ig6xM%2BiO1gAc4P%2B0CuPaoR0c%2FC6kxBRE%2B7Det%2BqTIPRGtdVDdmSdERTk8aRj09EBBjl15uUL3uXU%2FwyKrDgSRVRDJO3nUZ6PceeWkAxjn2rrULkI1tEd8wVzzU%2B9zUfBNT1t%2FOfKLaMcc4p61QLsMrvwt8NIwIHvH4%2BDowyIWdvQY6pgHumZMEHTYmHYfXL5aUNUZQr5GEaQpKVT8m8Ai55tz75vv2FYZPhTqCSGFpDMzTLsezUQIvrwzoB8Ulz8cQgC4h%2B4Enkl%2Brz0GITo2FTvUVvmhy%2BO520Owvx%2BFzPVAYUTQaerJ6uqDdVQOxf5qikyOtdOoaaig07KzAxxmGN90hRjspdxKLWn4cx5H6fEGnWbovPeE1TaZRj4cjrEmTumseO4k2YnDv&X-Amz-Signature=d3b430aa5c781039e7bb8f29220c1dd9989d51308b7702ed94f4447647e821b2&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652IKKQPQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA66tySQ0IYwO7%2FIi%2B9s65EIpa7mrXTGnSumNqVB1Y%2BFAiBFAGVt%2B%2FJdLleMTqurbqHOg8iMzQDAbicCklgOPHaEDiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vmP8ZvFhTv0xn3qKtwDz27YBxxN9Ck8LLniZ4mQGyR9qG0%2BmzvFl3vRVa%2B4POGDJtyOwdc0b1dl1j5Ht7RtIEeLGWImIbFnsY%2FVELpPLZMppLC%2FdUr%2F%2B7HwPDxMdqoQrvIjbrtC0h7rE4X1auOKdtyEqsTCcB%2FTRe6Ultp7CBJXNGR54N1cGMdeo7maKs5bavY1sq2eM4oF2kS14RmqB1ioGykxGnxwNKgAREKFOG3KNx52s%2FaViVY2hdJ6sao3gXpWAJ6VOcVgil0Z24hmO6jimuksxlthvaMB0tOoJR1c30VBWMITKeL6qp3DfJ6MouLIz8Jh3ciX1Rt7gXPQYnwI0nRTxxeennCh8sp1ZlG4gotKFwnzUgCG%2Fn41n0FYnicK2I%2BUxtLocMlKN1VYh%2B%2FVihYL%2FOFFy2unEgmEqSNIDncIk1cz%2BxZrkkuO9tAqLeksOGbqF1GUiRUvHmWMWDA9t8fri2nb5%2FQlrjHbP6ig6xM%2BiO1gAc4P%2B0CuPaoR0c%2FC6kxBRE%2B7Det%2BqTIPRGtdVDdmSdERTk8aRj09EBBjl15uUL3uXU%2FwyKrDgSRVRDJO3nUZ6PceeWkAxjn2rrULkI1tEd8wVzzU%2B9zUfBNT1t%2FOfKLaMcc4p61QLsMrvwt8NIwIHvH4%2BDowyIWdvQY6pgHumZMEHTYmHYfXL5aUNUZQr5GEaQpKVT8m8Ai55tz75vv2FYZPhTqCSGFpDMzTLsezUQIvrwzoB8Ulz8cQgC4h%2B4Enkl%2Brz0GITo2FTvUVvmhy%2BO520Owvx%2BFzPVAYUTQaerJ6uqDdVQOxf5qikyOtdOoaaig07KzAxxmGN90hRjspdxKLWn4cx5H6fEGnWbovPeE1TaZRj4cjrEmTumseO4k2YnDv&X-Amz-Signature=e32feca3851c58cbd1145e0b43916a69375ef7a8dad958ce4ddbba6cae68d8ce&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=2ef9655d20e4e6d58e2f16171adbbe4ad86584994fcce66ea0b4497946b53909&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=93c03cc79850d43c5118fb9aab0bda84845d1cfa3f4cac7f613871e632767bfa&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=a8fbb5320d38364d590db470feba05269e0fa58fa25588fe06b57158e9c745d4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=09a064b365d247fecfe7ea67b6278c2af267e09f728772cf45fb5b632ce3ad38&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=2a07eeba7390b19c61dff13bb4973ac43e98fd1c7ee88f41a9d2813ad4c6643f&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VVHXH23%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDm8%2BRHNqblVdJWipYXfnpfy%2F8PUca7oA5lhNM4OR2VkAIhALBCExImrlg73%2BuqAVjIp0hlHnLgYIQ0sDt2nE1Ig390KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxzcSRmbmfXs8ZAjnwq3AOr3v8HavxOJhWagBDJSKs8akvelpkZi9WTIOROKG7IprCIw1l5qVp0avM6z%2F7rSnX31fnemQ%2FhGp%2F3uqavnllXQTPIR1z1bU6Z%2BKjgTxrZeYwzH6mh2Q96fCMdpbgXK2ivHH6%2F2XMCBTWEMonoomhqnO%2FO07ZtzAGdcwjfZaF5ttMQ88XmK%2BFqnaeDjnGwnj9p%2FJbUBO1IeJgXj1L4QP7kgVDBiopZJcSadxwA0sU0rOqoEaEHDF8QddLB7e5%2BmstT7%2B1SMMAXVq9F2jwSEg8%2BUo5QvjDBlGqUqpelOhzLPDcZud3bTZaiAKVtoHepLnwjbFJuxPtOLkA1dPudf5D6ng0EiPd1ccOkwvlyLH3yvQQa0vgu23lc7z%2BY%2FhVcmwAa1YbggLV8%2FB%2FyxiyIhIhgV2b3FIJGL3boT%2FlE5eqxLxMV3Bi7kb90%2Br90JIlpKoSE%2B%2FWZtWYFsGf8FTNBOrIZL4VqEiRqU9rO5VQm%2FNYOqyHm7q8yzX7FMRuNnLCqkuphhfpD3gTfk2aOP%2F0ISCp6zuyhKrm9wJzCWFo%2FeYhbkRi32%2BNMZMcwwiDAhMwtH7HFzV8%2FoAb9jn3tAOwEJKEHTXqXRueqqhn5r4Yt0EGfAyomilrar%2FNNUqUXgjCJhZ29BjqkAe88lwxU7b4YFs8vhxl%2FokAziJFpQ5QOC3%2Frs9ZxZ7XPduujgg33YrOnaAveMG0i0Un%2BA2134sER00ABsd0Pp3eMFp83Wk9pyjoFf%2BcSCaIPHw4rBZXofl4ELHhBfHau9nkbinsVG8huttfVqzDEJ5SqlkvuzGm7rk5Cp8fgy9jFXIDalA%2Ffs0M6PUnHtoWNQ4N3ZJ%2BZRAXkDNgfMDiFX06xJkaS&X-Amz-Signature=89372a05c8c66bf50ddf3b0437e5e8be80855b6629ab1331c8eaf56b0c2f0222&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQJUGZ3L%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDJ%2BCgHhBcMlfD1aPSpuU7MC3FIy0NlhVeN8HpcyVhQhAIgOlchxawYHsNNq7gZKdWLmvAVbHOeBjBJxhwxPWLE6osqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH07YHoTB%2F90SQw9ACrcA3a7IAO7CGKNfEznoHT6QPra69pDHrSm7jxTleNAPffEf76rCpRppLpMNJ7oMis2lv5zQ5Z5UQVTIQe4Cw2c0EmlBCcz6XeUbOvidHtOkduvn%2BKDGbE92hXIHYPwrlIOTwkstb8Qf3KcFS3%2FoY4utlvWpFF0m0ZfN3eIpW%2FUHzc7k3kMLwmgb6nHjyx966Ee3ygDFa6nBUjhHlws12gTVZLqCfLp4udlSBbzWgU%2B0mWXZAfURfDOZBUZd7YP9NHJ0Zj3gNI6i0K%2BXZ3mhf8QXHaxvrNEprjkxsZwtjhv6KmoUxP3sKk9MY%2FVyjb1d1xWjZXwmBUKDqqw2AlWDMQl6xqzjZSBCSyJgMU2ErEKeEM8%2FC3Oskv7ko%2Ftjnv1gRxiF%2BH%2Fz%2B%2BkjMiLU6oWaQG9m%2BCsgZ6G0WInhR9dCMJfw%2Bcb05BmF08ZvEB%2Fwg8rd0j%2FGMmDlTdkExp5hrHf1ZW2Hdk7tAGbQrQ4oTQok4Pyj6cqf3BbEgFiQiAEYja1udKCYRz63a2aDmZpjnG1Rq5V5JCDxs9rQ9gAL%2B1RquDvJc5XfhHC1PedYF0urwRckMWzXwyptijNoYXGAapU2D5xZJ5gIgWLx2cAvjKXB6sN3SliaZU%2FNRCeNHwh1aX3MNaFnb0GOqUBUCAFiXxdwR9Ohpjy5eqA2uTDjcX1D24c9Lc65gboQxdwDLNPRepHHF7uHbEas%2FM3NaUXgHBOgUBz4ZM9FuNk34pQogRgATPh%2FJq59lZxVV%2Bw7pc0WxEpFZCZUKXdKtRYD8AfkAadEUWrgLnOUr1JH5whZed7YblwrhwXqVshAxV3DMFGlTwZzv9j%2FP9JDPvEVdOnjnMJriO8yxtaWDAuPg3FT98V&X-Amz-Signature=b06e9a097c878fb2f2c84d058b567031cad30a83dc60450777d7efae86b563fd&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQJUGZ3L%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDJ%2BCgHhBcMlfD1aPSpuU7MC3FIy0NlhVeN8HpcyVhQhAIgOlchxawYHsNNq7gZKdWLmvAVbHOeBjBJxhwxPWLE6osqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH07YHoTB%2F90SQw9ACrcA3a7IAO7CGKNfEznoHT6QPra69pDHrSm7jxTleNAPffEf76rCpRppLpMNJ7oMis2lv5zQ5Z5UQVTIQe4Cw2c0EmlBCcz6XeUbOvidHtOkduvn%2BKDGbE92hXIHYPwrlIOTwkstb8Qf3KcFS3%2FoY4utlvWpFF0m0ZfN3eIpW%2FUHzc7k3kMLwmgb6nHjyx966Ee3ygDFa6nBUjhHlws12gTVZLqCfLp4udlSBbzWgU%2B0mWXZAfURfDOZBUZd7YP9NHJ0Zj3gNI6i0K%2BXZ3mhf8QXHaxvrNEprjkxsZwtjhv6KmoUxP3sKk9MY%2FVyjb1d1xWjZXwmBUKDqqw2AlWDMQl6xqzjZSBCSyJgMU2ErEKeEM8%2FC3Oskv7ko%2Ftjnv1gRxiF%2BH%2Fz%2B%2BkjMiLU6oWaQG9m%2BCsgZ6G0WInhR9dCMJfw%2Bcb05BmF08ZvEB%2Fwg8rd0j%2FGMmDlTdkExp5hrHf1ZW2Hdk7tAGbQrQ4oTQok4Pyj6cqf3BbEgFiQiAEYja1udKCYRz63a2aDmZpjnG1Rq5V5JCDxs9rQ9gAL%2B1RquDvJc5XfhHC1PedYF0urwRckMWzXwyptijNoYXGAapU2D5xZJ5gIgWLx2cAvjKXB6sN3SliaZU%2FNRCeNHwh1aX3MNaFnb0GOqUBUCAFiXxdwR9Ohpjy5eqA2uTDjcX1D24c9Lc65gboQxdwDLNPRepHHF7uHbEas%2FM3NaUXgHBOgUBz4ZM9FuNk34pQogRgATPh%2FJq59lZxVV%2Bw7pc0WxEpFZCZUKXdKtRYD8AfkAadEUWrgLnOUr1JH5whZed7YblwrhwXqVshAxV3DMFGlTwZzv9j%2FP9JDPvEVdOnjnMJriO8yxtaWDAuPg3FT98V&X-Amz-Signature=fd55045b0b1875b8e353887376efa072550e2adfe7190fd9b16141746e6f7f59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z74WQGF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHl6F1QfhNJvb%2Fzwq7%2BzBNj3kvOP2LZjVK8b3XvwEkHaAiEAhbj7vacV4eGgDYwuc5Tj80rowquc%2BgEtxL1jD1cQlzkqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGeGkbUjim8XWWmxhyrcA9zRrPahkLHBS1V4M0v8k0PjIV1zKlcPdcJCI7WBCDHzHKeor8WsVz1Zy7Yc6xzeWbLvRbJwOzsKVgRsArZmIwblzHseOl1t31CJIZQX3SXWEJ%2BKG6iIMLVQ4epb9rcinjtMJILDTTNmgcTLac2mQmOrsF%2ByCiSctdt%2FlkeTjibI0Gh7WZxnjJlDP3otVCNcMTO15%2FNiyV2AnV6snzqbRj1Dll6RwOEw%2BEysycappi4xekknla%2BWUsq0C4wtb0kOSOzM8eEnMhjGQ97rIUsRInMh%2FUAlJRo5o9TmAnqvJgbF92CpnOHZ2tJaYifV4jDwYUXxc0wnek2MW%2FlrHBwfidM4F13ZqASjlf7EbUENy9CajLEWJ%2BhByMUNPGQscGSfXagj8IR%2FJ%2FW2lP%2Bsq3yfdaVWZIiec1TzAgU%2FPOsai%2FMtLT7xzYC5DbBjlfc%2BLpIc5uwwYhfe0Ldrw%2BkTXmBct%2FfOMcmSSd3Y6GZVArSr9n%2B3ycO9ZkbxjCRQpRoEyXTeDNKK7kKkzXMmH0Q0eBqJ0l7waezi%2BaFSuCsBYRF4DlU0rbRMIMOBAmjEQ3xQ6Hv7U0c2jqplwTuZPij1BQKJ4aSOPpAlc2MzqnVdCyz%2BmFluGyeqS851gdGZoDFiMLOFnb0GOqUBFbC3cVsoHDsAQ6GIkyveDxSGv6x90iG8Ic8A5AnqvNpnti9mDdRcHggn%2FeY9aGgDudw%2FHQP7%2BlC8%2FCg7%2Bmqm8x7h1X1kKCUoIrcSWpgmU5t1PUwwNvn797nw2Ru3645T%2FgjG5yl3OUGPj9PgfhOtUwbysXAi6yMqUhgMK2A4VcxV3U0ZtMnBrZE2CciIbWbnWROuZaaVIi3xdJ1avro1MCcg4L2G&X-Amz-Signature=dd33f7cc80e50d9ea85f51ffaf759c27d9cf1f7a24dd4279fe5e392d259c4932&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PTQRAZK%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDTVl1rCeYJS2y%2BCEoPOJ0gphf%2BUmBp6uKTtPWWpA4M9AiEAxGmcEY58bnIUU5fxuoSE9ScBIuYK2%2FTg6PHjfhOIhu0qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOO0kmgOqgtqGYPG0SrcA8ndlybR15cPAagvmd1U0oi5qiVnMZU9T9%2BOyH%2BF%2FdOE3Cgd6p4iqPva9pkJks8ZWJAF6q4Z8GOU4K8fBBHp5henQxB4HSa9Ogb9eJYXx7bDdY68JFbcZ7tPEJOyRSLFlIwkkC9hO%2BHFNp7w1oSjuPK5BD0PemMzGyKom0NpeiIfrDoJksi2ah56KA0%2FkAC7XgxuIefJqQGlT7D53P5cICia2ttcb3g8%2BkVhlWzHkDkSK2xIXnCuEzvkWhbIZP2RUFz8E%2BO8JqSY7SPt3hOu1DYstQW0TomcnPnrHBHKzGoHJ%2F3qqdDFuL1G%2Bgzz8sCFM8ANYVIbIQ6YfwpIjKPVTola5jQClT0JF6lQPLRIwqg%2BEEK85Yaq1ejtS2pSL4zPMCByOQjWxJ%2BKRJg8L6V29RLpNkjtA03i%2FoT466Cmg2GCM%2BaWnAJha2tuS27CutjvdsAUiuISEebkdwCDIq%2FmCt9Q%2FD72bUFbBJJyoVfeVdD%2BaXxPeF3L%2FlXusP9xR66k5duANTmSFQY4kgRg4AprGDxujpzxhabpz4SdByZ75VR3zu7ftpHv9rTCz5OoPKqUGc3SjEmhnEyG1895%2FKf0X2m7A78wKm9EIZNk%2FHoYFSUgmEINvA8YNsAbE6xJMN2Fnb0GOqUBJO%2FseuoEe78Q2hjP53rQT5jaeX7FTrdLCYWWN68Asvi97Z4Gqve%2BG%2Fne%2BW22wJwDPe%2FYJ8jVKLNm7dyifN3K9fR2L2fegoGlBwmwZbkBKAGHzwbqBSJm5ozPATF3z3BTkCSdjGKwpxCPSMwEgC%2Bz49SIJ1eq%2BMY0hy1piWkVwj3nSlaMfSn%2BF3OEspntLaWtpc8rrXNBnFJSS3jUlY5ZVMZgdG3h&X-Amz-Signature=f8bfab7454991f7c557e76520263f0dd1dd19f52d3046834e5a8f35c844cc7bd&X-Amz-SignedHeaders=host&x-id=GetObject)
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