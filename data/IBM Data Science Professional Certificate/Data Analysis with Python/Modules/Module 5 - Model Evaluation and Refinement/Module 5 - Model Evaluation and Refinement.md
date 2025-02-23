

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=a2685d7d03d7844322016c8d33ff9129028e1979a6391adbc4f5dab11e79bb67&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=f1b98312abccda449f932dac644c8a49f1abed071ba852689bdddcd767832101&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=2f74f4a8564e9f752a4096913c48b06b5b35940cbb51f8804a8f8c5d994e0587&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=cb93e34c3026d819483158a83c968a0c0c8d52cd7cf22330286bfad6da0513e0&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=9ab5dfd3b3e3ae203a14d82309f6bc6f2fac22366e3f618bf3002ffddb87f2d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=3d09cca490bc04aed182674fe9e6a0ffc3f24c977ba34208bb5da70f50f1a0d2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=6c9dbf50adc2ed51bdcc5485442458a1e33921942b12c663de6f222a489798a1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=dbc9cc43aea1ed08ac695a5c53cb289f2e5114a87b508eb8b1e51a9b3160be00&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=2fdcecfacc86242e680a518baecab938d43231a3f5e1a2a1d9f190570863b9e1&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6SWBCU4%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZKoTKZp%2FolhX5iyI6culkB%2B2iwkkLkjCdJZsxBEbCVQIhAJSFgY%2FqE7fJzMquRlDKmu0FUbqaeWasbrfcNyxEvjRPKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9mf7gid4jKcw6iGgq3ANHV9diN2VZRrnRGaLQxqawBJQ0DmBx5nWR9xkKWgVQWSEirMnouvYi%2FnWqyPxLkQV7j4YCodvIX8%2BeVyjxBZuBJ33SuQ%2B8wOaJGXQxWrXO25tBWtfbs84a3k5GDjdfOkk4PMTerLzHWFrtSq8CO2ZKrEz2CyAxY%2B%2FkAFY7PrkOYNGd6yb7Rp0aF8rKaNGDQ5guv5MDd%2FLWrVLy4bgjAL3tSaPZg29dgUndy9a7ilTohQXsRpniMSlgVZeTnHuCm62TayYyJYYwU9f7ubnGapKxE41VMRCw21lJfWZ4Sqfbs9WYUBCFsDVd8rfQ2Ms9IoBbHMM%2BazQ99QtItC%2FD4wBSZCjHhPQY1oTT9vJsDIotPpsNnljEqkZLZVPhmVO6wrZS4%2FVDwJfBuRtojSA4V9lnIyuCTIpnoWFdttcZluElfov66W6w3%2BcAxfSRCHHhZn89Ynanv1swB2istuifZ4f4UmpAXBSAMsGYwjH6rMzyXtFww9EE4gegJgGdbwnNuCX6vbolwSqR2tDQ4Hl73PDi3XWY3UkieDy5Mf8aQpbS%2BvCDpjwS88HRG50DEAsMBKsJMmupMRmv1PLdo0raxM2rdo%2FBqEb8z2clmQGupuztoXsJJoGIGE5s3kRssjDMsOm9BjqkAQypg1yrk3%2BK%2BpDyd5a%2FpafBR96YL5wcZ0eMA3SBkevRMJPdiHs6RC2z%2FDJSMxKJ1ClP5jdxestt4t6v5J9Eww2WxA1BX7onK9Bpwuq%2Bc2TT7VvyGTivdnaelq6az%2FqV6GJo3AKBSlvVRC6JQQDHrPWCQmdzM%2BJTuXaYM%2BKn6L4QyCp78B89xMV8mbDLGGWK%2B7vADKFEqDr3m8nz2HGUDt1c%2F%2BmX&X-Amz-Signature=f324ad1c09cb9f70144c5ad934ee7d2ebef65fa2b79a2a80f3c83d17d4a917d5&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6SWBCU4%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZKoTKZp%2FolhX5iyI6culkB%2B2iwkkLkjCdJZsxBEbCVQIhAJSFgY%2FqE7fJzMquRlDKmu0FUbqaeWasbrfcNyxEvjRPKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9mf7gid4jKcw6iGgq3ANHV9diN2VZRrnRGaLQxqawBJQ0DmBx5nWR9xkKWgVQWSEirMnouvYi%2FnWqyPxLkQV7j4YCodvIX8%2BeVyjxBZuBJ33SuQ%2B8wOaJGXQxWrXO25tBWtfbs84a3k5GDjdfOkk4PMTerLzHWFrtSq8CO2ZKrEz2CyAxY%2B%2FkAFY7PrkOYNGd6yb7Rp0aF8rKaNGDQ5guv5MDd%2FLWrVLy4bgjAL3tSaPZg29dgUndy9a7ilTohQXsRpniMSlgVZeTnHuCm62TayYyJYYwU9f7ubnGapKxE41VMRCw21lJfWZ4Sqfbs9WYUBCFsDVd8rfQ2Ms9IoBbHMM%2BazQ99QtItC%2FD4wBSZCjHhPQY1oTT9vJsDIotPpsNnljEqkZLZVPhmVO6wrZS4%2FVDwJfBuRtojSA4V9lnIyuCTIpnoWFdttcZluElfov66W6w3%2BcAxfSRCHHhZn89Ynanv1swB2istuifZ4f4UmpAXBSAMsGYwjH6rMzyXtFww9EE4gegJgGdbwnNuCX6vbolwSqR2tDQ4Hl73PDi3XWY3UkieDy5Mf8aQpbS%2BvCDpjwS88HRG50DEAsMBKsJMmupMRmv1PLdo0raxM2rdo%2FBqEb8z2clmQGupuztoXsJJoGIGE5s3kRssjDMsOm9BjqkAQypg1yrk3%2BK%2BpDyd5a%2FpafBR96YL5wcZ0eMA3SBkevRMJPdiHs6RC2z%2FDJSMxKJ1ClP5jdxestt4t6v5J9Eww2WxA1BX7onK9Bpwuq%2Bc2TT7VvyGTivdnaelq6az%2FqV6GJo3AKBSlvVRC6JQQDHrPWCQmdzM%2BJTuXaYM%2BKn6L4QyCp78B89xMV8mbDLGGWK%2B7vADKFEqDr3m8nz2HGUDt1c%2F%2BmX&X-Amz-Signature=cd940707734b6a954bd94c62120a4fc445a74c22633b060ec5f08ca7103926d0&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6SWBCU4%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZKoTKZp%2FolhX5iyI6culkB%2B2iwkkLkjCdJZsxBEbCVQIhAJSFgY%2FqE7fJzMquRlDKmu0FUbqaeWasbrfcNyxEvjRPKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9mf7gid4jKcw6iGgq3ANHV9diN2VZRrnRGaLQxqawBJQ0DmBx5nWR9xkKWgVQWSEirMnouvYi%2FnWqyPxLkQV7j4YCodvIX8%2BeVyjxBZuBJ33SuQ%2B8wOaJGXQxWrXO25tBWtfbs84a3k5GDjdfOkk4PMTerLzHWFrtSq8CO2ZKrEz2CyAxY%2B%2FkAFY7PrkOYNGd6yb7Rp0aF8rKaNGDQ5guv5MDd%2FLWrVLy4bgjAL3tSaPZg29dgUndy9a7ilTohQXsRpniMSlgVZeTnHuCm62TayYyJYYwU9f7ubnGapKxE41VMRCw21lJfWZ4Sqfbs9WYUBCFsDVd8rfQ2Ms9IoBbHMM%2BazQ99QtItC%2FD4wBSZCjHhPQY1oTT9vJsDIotPpsNnljEqkZLZVPhmVO6wrZS4%2FVDwJfBuRtojSA4V9lnIyuCTIpnoWFdttcZluElfov66W6w3%2BcAxfSRCHHhZn89Ynanv1swB2istuifZ4f4UmpAXBSAMsGYwjH6rMzyXtFww9EE4gegJgGdbwnNuCX6vbolwSqR2tDQ4Hl73PDi3XWY3UkieDy5Mf8aQpbS%2BvCDpjwS88HRG50DEAsMBKsJMmupMRmv1PLdo0raxM2rdo%2FBqEb8z2clmQGupuztoXsJJoGIGE5s3kRssjDMsOm9BjqkAQypg1yrk3%2BK%2BpDyd5a%2FpafBR96YL5wcZ0eMA3SBkevRMJPdiHs6RC2z%2FDJSMxKJ1ClP5jdxestt4t6v5J9Eww2WxA1BX7onK9Bpwuq%2Bc2TT7VvyGTivdnaelq6az%2FqV6GJo3AKBSlvVRC6JQQDHrPWCQmdzM%2BJTuXaYM%2BKn6L4QyCp78B89xMV8mbDLGGWK%2B7vADKFEqDr3m8nz2HGUDt1c%2F%2BmX&X-Amz-Signature=4fbcd326a4f332ffe6d038d47322e4d88637a87767058839dac02b48e6852664&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=e57f880e39e5dda0aab5926d534cc1f403016cc365625b1f259ecdd057151df4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=06106f6f6bc212af8f4aea6a31ba8ee21026e6a813b2709cd9ada038f5771242&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=cc287b0df35df2315301494bda5b364cf3be86878e37e43e0614e2fed4f2db01&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=3a559e1db5d0586dbcfeac1f04e4fbe7ae5a68965df9ab639f5f7d392a4219e2&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=89e9a74f0dd15bf124a6d28d8e1a7828c686350d6ece366ba4c510fbe4202386&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMH2NGBD%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWje1kpUNnSzRatU1k6%2FEmb0Ss5jr8Ut9dPOUSH62tvAiBDYh1PjyzsoKVvG1G9XEyG7pEWx1NFYKRG3mdcwUS%2FpyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMliPnbkHI6MVik%2FiNKtwDl94OZksXFiIRFuLsuGLPRyy%2Fc0KDfWtrnRFZc7BUggJwcURkV%2Bsb%2FYiVf2D5d1skxWMDvuJ3O2N4R7jBZ0LgPBNGUPwPWQBXSmZzS95mIxlDkQou%2BAMQmDodj2gSkoW3yZ8uH4n1M1K8J4OxZTgp7p9QeaNsXO6ExMKPwYy%2B88Cwn8GA3lji0iJgCMbcas70baB5hhutf0rzqXOLb6rDRuNhlDYT00XDLsZuD9ltt6ulZnUcT7VV9tw5hKpXW46tWqh0Y5q4I4MWJ7k%2F0KgWI3kd0QKqQroNr1XuqY3xCtcLkmXxT3VdiheRuLGoYLHEAv9BZP6E%2BJrvQ4P2bK0nm6yz7Sc3qikkZDTzzF5zHOeEWkY9E%2BurEHnYvLYKGztO%2F4TfZK8s3SNLKjYqxPIucK2uvLkKNNOm%2F62VUNUiTESXBJLsAcbxdfzpv%2BuurzVAulbSR26RDwyfKF98XB%2FbDBEsV1j9ohmdOAUqpminLlXhgve3jk8jan9E3Te07Aeih37U0S4ChEatN4fS1dxptFfzsY42%2Bs1iC1QLVaG8vY3xexqSsDZWU%2FnLDC9VvSNpBprNA1ieeltmsHvo1eMyyA6sK1M4y80nHQI66n%2FB%2FifCwO584Nzr2HEZTyQwq6npvQY6pgHT7AXRdfOMSZZ1jBpL2g1DZbifCm4p2inF7GnijKYIWotfAgblYs60FIrbda49sTOgRnh30N0YLp6Ma4HMuBet8B%2BFuhp7pO8qgq77aqJlYgQPRZgKVLigTLskweX4UNbziNWdiBCX28Yk36TlIJtizqq8%2BqDb1GZc8xHb8jLQkbELqnm0CHYA5MqeVisn5OPpJYJ5swTulk9m7fe70%2BF2YDZSr4R1&X-Amz-Signature=e1f76f47b6a8d51822462d949de81cd14a2f94ad8b6dd74bf9e60e786072a1da&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2ZKV4JG%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA4%2BudUi%2FmxAbKv42khKoa0r%2F3tgkgGXTz2dp%2BhVTkAtAiEAx6e68zWqJO9OHqCzj%2BHiubRYWzOegOnUPZ1K%2BeJfW5IqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEKgDft23nUdtvGUBCrcA%2FWwN23O%2Fp1qlxpFRtLoGGlOgxo6vR%2BqEpBpoGb6y99sbkhBzMfhHyj5MqcPvd6ZOD4zDBUXZlS%2F5jQ3Xp1h5VVjFj7txFue%2BpSTkp2sJ5LwQh96cqCHDjn6zXrut6mwZaRrSjI1i03KnPuxbKvFwqq96BL%2BSx8KNSbi8i%2BWFJkAaF0E9P4%2B4rKxbbRSsMMTYrewWZ8o7ZC4hLulOMV%2FBYUSZ0gLdhMoR%2FNAOV0gDjQ0fJdSC9TkHu8GwtNmVm3n9dwHnude8tDeja6nYKLniZOSAMRFxKrg71ogf7DYaZXycii63O4NvjqbnoavGPmNyzhjk7Hd9CklDF4ltvzHLx7sd6I91AXchOZX9BDHGefeZes101kZOC87JG6m7XHY7BKyIosdlQtq%2BgAzMUXhJU0zDsGP%2FbMkC7iWtsFUr29waoddyXilElBTe7pHjD5JXTON0YbIwZ32MGNv97cdDTjiKSHB6aSr3XaLcv0OwvpJh0dNSUko%2FpawBm%2F4bcqkwXgjxQXi7hmQ4hq4tFIshyhxKsD668DDjaExbdyazK%2F4C49Mii0xouu11eX75DzyNbaEyqCZLcqJrkM6D5k43DWiWBwdLR2tAXsWwzxZ57bPh8dEo%2BD5YnKQyK%2FtMO6r6b0GOqUB5NE5cO0131V%2FqCiP%2FCV8B71ICeOplbKDo2PGcp4IdNwVEw8%2FP0QQljakfqVf4o9s19t6WYuaNg5NnypxWwM%2FOCUIOOWieU8TX0tFtUm9NbDYHfvFD3t9zk2f95B%2BtVPWpEF6mvW%2FhwbYdFcCa08bidfSeXWscy97W%2BwITrDofvUxBxBZPcAoOHbWYriIQPWmoCrzt6YSEA9iQs6DLyk7weOXDMzj&X-Amz-Signature=cc9a7668710556b44146bd491dd59722eb008dc0d201935e2c3f6bdb5de69348&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2ZKV4JG%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA4%2BudUi%2FmxAbKv42khKoa0r%2F3tgkgGXTz2dp%2BhVTkAtAiEAx6e68zWqJO9OHqCzj%2BHiubRYWzOegOnUPZ1K%2BeJfW5IqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEKgDft23nUdtvGUBCrcA%2FWwN23O%2Fp1qlxpFRtLoGGlOgxo6vR%2BqEpBpoGb6y99sbkhBzMfhHyj5MqcPvd6ZOD4zDBUXZlS%2F5jQ3Xp1h5VVjFj7txFue%2BpSTkp2sJ5LwQh96cqCHDjn6zXrut6mwZaRrSjI1i03KnPuxbKvFwqq96BL%2BSx8KNSbi8i%2BWFJkAaF0E9P4%2B4rKxbbRSsMMTYrewWZ8o7ZC4hLulOMV%2FBYUSZ0gLdhMoR%2FNAOV0gDjQ0fJdSC9TkHu8GwtNmVm3n9dwHnude8tDeja6nYKLniZOSAMRFxKrg71ogf7DYaZXycii63O4NvjqbnoavGPmNyzhjk7Hd9CklDF4ltvzHLx7sd6I91AXchOZX9BDHGefeZes101kZOC87JG6m7XHY7BKyIosdlQtq%2BgAzMUXhJU0zDsGP%2FbMkC7iWtsFUr29waoddyXilElBTe7pHjD5JXTON0YbIwZ32MGNv97cdDTjiKSHB6aSr3XaLcv0OwvpJh0dNSUko%2FpawBm%2F4bcqkwXgjxQXi7hmQ4hq4tFIshyhxKsD668DDjaExbdyazK%2F4C49Mii0xouu11eX75DzyNbaEyqCZLcqJrkM6D5k43DWiWBwdLR2tAXsWwzxZ57bPh8dEo%2BD5YnKQyK%2FtMO6r6b0GOqUB5NE5cO0131V%2FqCiP%2FCV8B71ICeOplbKDo2PGcp4IdNwVEw8%2FP0QQljakfqVf4o9s19t6WYuaNg5NnypxWwM%2FOCUIOOWieU8TX0tFtUm9NbDYHfvFD3t9zk2f95B%2BtVPWpEF6mvW%2FhwbYdFcCa08bidfSeXWscy97W%2BwITrDofvUxBxBZPcAoOHbWYriIQPWmoCrzt6YSEA9iQs6DLyk7weOXDMzj&X-Amz-Signature=3af32ff541f3640c9dda5183b52662f53dd721091f40e06ccd68b1d8211bcbcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AGSXT54%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJzZqXVcUetn7PaqQMmlgNF%2B0MX%2Fkc9zKCMfF6eY%2Bd8wIgbtitjYti%2BhqPKCdoaNS7hgDVY8dd8zjHoGvegnkLZYMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDn9SfD%2F9Mrx%2Bm7CwSrcA7yEnS6Xbqss%2FF%2BEAu1TUzudatNjr1hJIqaDhibka8tNQYhEyHwMFBHUAAcUEJOmYSnlg3lW%2BcYxIxZmivXkCk4IB9NFwaad9mTKSvyVqXQ7xAXrC9MhlF1JxAlvkQNUMkWgb%2B%2FC%2BSkadrlo4%2BPTio%2FcYkc5Kmw829uwWLJB27vKuxk4x6w7%2B6kjys%2FnEvSTT1PMYrIPZljZemY4eXraXmghYOPatmYMNRPCz%2Fvj9os6TqOgNnmrQb7W47Vv6fPY0uFQwND5dLkKS%2FrxQCViscOBqR3ofmtdkOiJNu1L3fmIEpix%2BELcMpCzfXemigIV%2FtYbUaXmAtk9HfVJQmwA9l%2BydGEJb22DQbzw8WTDuMtXiwAefdEfa6DUDKWcMo8rN3rlvgGoaUdqBZIO%2BrhnJgRW1V2QVU6MIh96kD%2FH2qsUlcRRJfbuqDp%2FNZ6ThWs7Dxl7J53ycfO6Iw7X50StOBRQ31jt5cwrvqbgH5hsqBh4cnEDpkCcQoF4XuHjA1G9MdqZpl4XXJ4E%2FnYhe%2BILn73fNNDwNpSetUx5e5R1zEvv%2F7jhJeHigoOdvYYWrVUQYBsgXAUzEfF%2Fr9sJECexeUjxdE0oDPQk3qMIx2mTESYAmXEuEw3NC2OMtsDCMIKw6b0GOqUBJYqwonKQu4O2xz5sbpx1wP6QEsDshjfEwBLLhjlOtPMnMmRgah42nja17CBw%2BUx94VYE51MnbimFuVopL8FRRfgrPXq6aq377ZtUFA7hxYIIRFTJs9eQq%2FTA7Lw2I%2BDPqZVlLHws3iIKOZ7x1zYjb3RLqaIcqdunuIek3hWN5H79oVPoEBVcy1PfjxHe2xBo02ONAMDnTGRI7KBpQs6OLCUbHWqC&X-Amz-Signature=de1adb669b3cdac79635c2dc2e5c1b4b1d801a8f5d9812f0d504acbf330612d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOL4WGPT%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDmUWrYF1B%2FMjEbMWgLIgtHpR%2F3WfWPMKZEJQLScxpx7AiB3UmH5WkPB36a8d9q14E72XQy8akFnWQLQ5ew5UbXIjiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpeHoQK1lDIV62eyIKtwD%2FfvIpUcK4H89oV09daQLaG3rJ3nw27xImkYCGhavMlreL3G8jhlGBUMiOKq6b0qeC5GU8ZKBHSgQwI%2FYm6ES2MJkfD8REuEqzu3Z2XY2%2FLOodOn%2Bfd5660Cd7I%2B2m8Er1B0GvybzjOtE%2F75v9%2B12YCtB3Q43M0xewmzdlGmVh5zicXKZFsoWrRS7L85xE4cauY6FDw9LUsEcDTUhhlCLh8xhUUM0P0Y2Zszi1EWBNaW3hhq49YW5Rcf5jb%2F0y5uLAqqW7PPM77An%2BczksYnGDULm8h3yooVvlBVASc%2BZRORONw%2FuMCDhVG5ebfKo2dBd1YZe6oUC%2FkxKOxXbO4IxXJCt3mf66e%2FoXDcSeZi0aR8nB0%2BDw%2BOxAbGQhtHOr6AeY%2F3Giylz5a9oJ6o%2BRn%2FQQYIA9SB3tYu1uMaHnFOK5udUJQENFQY9%2FLU03Y%2BXuB5KNmpFY%2Bw5w5wdF2cOkMbEbp7MGgPUk7gQwLQv29TbT7bJULElI6f%2FKES7zaZJ7mcJEUX7jx6mwszJP%2FJj%2BX6IcVQpdeFm%2Bqgc1%2FZzybeQTVXb38fcg60%2B1vbG6BF5rpQ4XbieiT6aTBV3lZ5IWh2hWGSWySaO2SuLYSUkuPX1FiInqrUafYHLIcvsJU0wlKfpvQY6pgHpqcfwsvW3enXw%2BC9p6FYfceh3uyf8I83VNA4W0wiG0mFIkdBrpLoSi5fLW7lgVjr3Aoh1rwiB%2BU2MEye6m%2FZSfVfN0i9YXpAxiSCaaXXLnQOSqotUI062XxCDjd5PBIYnuhV9cULmIDjABX227dPPOAmpN89PXETlJIdrTmXoZypcj3ht1KZUiyWuVfznV6IiGTmrCyVVwVvS9iugSKyl4Ga6H1fe&X-Amz-Signature=52435b4110437a9491d197b3bcaa475340aece96bda4aea4475536d6222b2b31&X-Amz-SignedHeaders=host&x-id=GetObject)
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