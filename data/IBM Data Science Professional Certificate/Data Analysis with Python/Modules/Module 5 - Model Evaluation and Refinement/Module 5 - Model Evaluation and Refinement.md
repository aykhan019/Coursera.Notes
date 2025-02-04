

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=719a2be76c1b91c73d7c0862f006d1bf0c38a04979ad702f8f031536a3720336&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=3b5f24a01a1eecf44a069964411e67786f68a58c3f2cf17b6e981a12f2c7ca1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=b65e8b6d3f34993b61a8e0e5278755817d9a1b0c06f47b9406b813b1f5bc676a&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=550cb79a1fcf0ea20b2e99ed795398cfb81b31adbf0fb977b04069e3529c92f8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=39c068c72499ec52c79738987f3043d56a7399e23a29169990efd06e94af4d4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=01394b738140c484f65b3d714d574749ed4f2f018b8737de409f83f825eb7177&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=4f74d1fff336d69c39586c5e7d484e32a6744bae830f92cfa91bf1920d849c8c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=f3892a2da405a4c309b20b5596d78143051beaac80a33cd7d33eaca9222bbb68&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=a8bbaea958319fcc3482d63670db4ce037af7f88df31b317eabbab9271fd2ea9&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJBMZBT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDRaTFS3OQS71hswyzcZ6JSDR2aG1g0YzrXlYBXPayzaAIhAK72FMBKWQDe3fEBDsIHRCxVZxmf48%2BAp0v28fTuQgQYKv8DCDcQABoMNjM3NDIzMTgzODA1IgwQVFJmm%2FF5hMUD9Hcq3APQU%2FaM6KsenBt3KLctX9eqC2GK3BnzHjuT8oq7aqODvYDEgxfS9OXJV%2FQh16JIDGhADAIxuM6pCb1JJ%2BiSTpd31hl9qiNLZu24y%2F%2FwYjCis9Huf9FE4ppbGp3I7WFtxbJX5B%2FwnenMzUnrViCgcSauDRxGbFdppNVn5Q30pfzW%2B8mjOWlTPjcrG9HNtJw%2BxXODogXa6S%2F%2BubIXE9pDzOXeBRCDGWPnhfFiqqi3%2BxIGfbK%2BQLpN%2F4OzHqHVpQeKLN233MmrYigZoyDENAnCcbvxwHJQTO02TykivIG6Pc7WMe05PDxeycoINqNxCgks%2BLAUmdUGCLjlRZbraudnRtKVp7JTCO7vg361nSKqQDIudrBvd7zOTdXVoH%2BA%2BOhxzgXHZOTsQbyXEYmx09DrI%2BeutceII0zHWB6NaPuOBxr3gCdFjiOz2QGxJX7CGweRYFMO1NkwPkEI3KJABtcGb9pbDslmlGLU6sRau2JncU5d%2F2BvaVtv3TR8lAhoUnNPqSakaKtcIcd2DWcIE2Ou8O8DUjJ5sPxQplwGIIt4zb2Rj3hwDLA0BqZaFxV4s69q6b4oXXvBX6meg%2FskWUFjY%2FfiI0h7kd91AqnKVAYF75GobBD4JASp6AxcpLBxtTDklIq9BjqkAVOqa1IL0o7SrnrTGkUbWQt3gxKPSiDVZHpE1%2Br8UEVVikAX3UIGYTdWK1VXiH3e3oZ%2F46wIepvQtsiDkv3n9gCqR4q%2FEeAZjmbt21i1aY2syVSeNjF%2FaarwwyeNpnGzuOKWENzXaBo9zeEbme5RxsibYFpHXyl8MhaWUt%2FPRw%2Br75hVS2IB145Xw81XAkYe5uAAQ0kcrovmjIh0qTTWYNqWUquT&X-Amz-Signature=5e22db744f796624a0855c24254de4169de007fc181c1c3b54bcd76630256939&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJBMZBT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDRaTFS3OQS71hswyzcZ6JSDR2aG1g0YzrXlYBXPayzaAIhAK72FMBKWQDe3fEBDsIHRCxVZxmf48%2BAp0v28fTuQgQYKv8DCDcQABoMNjM3NDIzMTgzODA1IgwQVFJmm%2FF5hMUD9Hcq3APQU%2FaM6KsenBt3KLctX9eqC2GK3BnzHjuT8oq7aqODvYDEgxfS9OXJV%2FQh16JIDGhADAIxuM6pCb1JJ%2BiSTpd31hl9qiNLZu24y%2F%2FwYjCis9Huf9FE4ppbGp3I7WFtxbJX5B%2FwnenMzUnrViCgcSauDRxGbFdppNVn5Q30pfzW%2B8mjOWlTPjcrG9HNtJw%2BxXODogXa6S%2F%2BubIXE9pDzOXeBRCDGWPnhfFiqqi3%2BxIGfbK%2BQLpN%2F4OzHqHVpQeKLN233MmrYigZoyDENAnCcbvxwHJQTO02TykivIG6Pc7WMe05PDxeycoINqNxCgks%2BLAUmdUGCLjlRZbraudnRtKVp7JTCO7vg361nSKqQDIudrBvd7zOTdXVoH%2BA%2BOhxzgXHZOTsQbyXEYmx09DrI%2BeutceII0zHWB6NaPuOBxr3gCdFjiOz2QGxJX7CGweRYFMO1NkwPkEI3KJABtcGb9pbDslmlGLU6sRau2JncU5d%2F2BvaVtv3TR8lAhoUnNPqSakaKtcIcd2DWcIE2Ou8O8DUjJ5sPxQplwGIIt4zb2Rj3hwDLA0BqZaFxV4s69q6b4oXXvBX6meg%2FskWUFjY%2FfiI0h7kd91AqnKVAYF75GobBD4JASp6AxcpLBxtTDklIq9BjqkAVOqa1IL0o7SrnrTGkUbWQt3gxKPSiDVZHpE1%2Br8UEVVikAX3UIGYTdWK1VXiH3e3oZ%2F46wIepvQtsiDkv3n9gCqR4q%2FEeAZjmbt21i1aY2syVSeNjF%2FaarwwyeNpnGzuOKWENzXaBo9zeEbme5RxsibYFpHXyl8MhaWUt%2FPRw%2Br75hVS2IB145Xw81XAkYe5uAAQ0kcrovmjIh0qTTWYNqWUquT&X-Amz-Signature=93468e5140abc1f75a8b2980958bc0d1cfdd94f08e12da5e040bc5ca68d72508&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFJBMZBT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQDRaTFS3OQS71hswyzcZ6JSDR2aG1g0YzrXlYBXPayzaAIhAK72FMBKWQDe3fEBDsIHRCxVZxmf48%2BAp0v28fTuQgQYKv8DCDcQABoMNjM3NDIzMTgzODA1IgwQVFJmm%2FF5hMUD9Hcq3APQU%2FaM6KsenBt3KLctX9eqC2GK3BnzHjuT8oq7aqODvYDEgxfS9OXJV%2FQh16JIDGhADAIxuM6pCb1JJ%2BiSTpd31hl9qiNLZu24y%2F%2FwYjCis9Huf9FE4ppbGp3I7WFtxbJX5B%2FwnenMzUnrViCgcSauDRxGbFdppNVn5Q30pfzW%2B8mjOWlTPjcrG9HNtJw%2BxXODogXa6S%2F%2BubIXE9pDzOXeBRCDGWPnhfFiqqi3%2BxIGfbK%2BQLpN%2F4OzHqHVpQeKLN233MmrYigZoyDENAnCcbvxwHJQTO02TykivIG6Pc7WMe05PDxeycoINqNxCgks%2BLAUmdUGCLjlRZbraudnRtKVp7JTCO7vg361nSKqQDIudrBvd7zOTdXVoH%2BA%2BOhxzgXHZOTsQbyXEYmx09DrI%2BeutceII0zHWB6NaPuOBxr3gCdFjiOz2QGxJX7CGweRYFMO1NkwPkEI3KJABtcGb9pbDslmlGLU6sRau2JncU5d%2F2BvaVtv3TR8lAhoUnNPqSakaKtcIcd2DWcIE2Ou8O8DUjJ5sPxQplwGIIt4zb2Rj3hwDLA0BqZaFxV4s69q6b4oXXvBX6meg%2FskWUFjY%2FfiI0h7kd91AqnKVAYF75GobBD4JASp6AxcpLBxtTDklIq9BjqkAVOqa1IL0o7SrnrTGkUbWQt3gxKPSiDVZHpE1%2Br8UEVVikAX3UIGYTdWK1VXiH3e3oZ%2F46wIepvQtsiDkv3n9gCqR4q%2FEeAZjmbt21i1aY2syVSeNjF%2FaarwwyeNpnGzuOKWENzXaBo9zeEbme5RxsibYFpHXyl8MhaWUt%2FPRw%2Br75hVS2IB145Xw81XAkYe5uAAQ0kcrovmjIh0qTTWYNqWUquT&X-Amz-Signature=abbd6ea73ca4c3f6b6af929a092dc8b0098afd90fbb6a90786ba9c5cc11e1c12&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=6475c62b2fac50897d6ae211afecaa70a693d1ede2297245c060eae106943221&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=26305e77eeda9e6a0d6219c036cc4aaa11b8965b4ea44413537a8a17dd09e3bd&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=8e8f646ed033d803a45bc059e5e1d5e8cc739396468644fa0209700f447ef3ac&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=c34964a4da87ef25c392e526eed313d3f0be051a39725770b4ea77105c1b7a08&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=7d6a351d7bf0794a2d65e6048a1b80e44d6110be3c0e9332a18edfc7b6b15849&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XYQJH4E%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQDXvwNXxKKbxUKlZ9OzGjGZi8DovPEzCY%2BGKYrVsXdqaAIgERrTgi735%2BUO9vRRHFBb65mdiOOsnKvBFWrRIhWOfC0q%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDCk1Cd606PnoZHcx2ircA%2Brbb5K45LYTFO2oQfpr2awZ71BJvPy%2FIf%2Bg7il1QcvIRUmlChFibx4EbUGaZ5WB3Uc%2FvmrWdVnjFMJqFjT1CNl6iFpOEgAyMqNoZEThlb72cd73SIDvzJAPGVyK5dNUj%2BMHF%2BeI2UrpMr2HgZiQfKqNmAjybj%2BvqmN9sQesky8DzSOa6AWWwDlxrN%2B9%2BnqRBnwcfHWR3%2BuRnPUuDyUJIcv%2Fhx5VkuD6dlW713dl18FKyfvNKjvrzu57u%2F1w0sAqo58nyKUex%2FzMXYy26d2D1Y4gKms6b4eWz%2BBW9bmSfhxlCtlOos22s4ZKlk2adukeRilBUqAIt6hr9qhXr8UukjlVvRXAx%2FaWyIJY%2BEhlYGy1nji6H1N%2BYyl%2BerrYvX3HqDy9myhd4pWwRC3428zo2z3uU%2BzysJhlCPch0DMtVe%2FJcKWeHRRfey0cFSgo%2FgRi9SgHmmmp3Q45PQvZp7m8eGK6NfU8tjQoHwaOTrt5UmtYp2ufHHL%2BSNNkWWQABp5X6e9p7ZoK7PkIm2NPvzaudoEmZc36vNBj%2BL5TfY0eaQacbHCuBpTFu1eZPciV%2FHIxcMyDPycBg5EzHZh0FASIDjYmJ6pcIe8SuVb2jL0PsUvxuGIcVxpS3Iwgd2RHMP%2BTir0GOqUBmIw94QcXtdXbrzcf6jX9zQmzroCc79cSdrBOaTXERZ9SIovYVU0xnPRsRzsmWqFN7cZYDnXLydUlq%2BTOzaOEzs9tKZdeMTUZ0WQr4y5nJFgC9gliKya1a0Vpw6rJFZ2XRY%2FOFJ6%2FaK8ptjRB%2BBoa73aGLsoT%2BvFNpK8WA2aSCV1ABwkA6EGSe210n7jTDR05HaFieipt%2BkCPWwCAfiu7LBKdptaI&X-Amz-Signature=9f14072c02fe8086d5f1fa393c20279e15abf74371a38224f847f86392df0afe&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673G4MBFX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIAQJ8haFJCMPNjFRMh6rJDBD1h3m5L4is5SGRJFBh30HAiB1TQ4iLzfcO0GTMZPDEdSp307KWouog60vpm2XzjXsUSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMAyWQeucaoqaRxm3UKtwDgKzE7xtQ6ycrm7bQlFAGQXG4hfYUjJRDgO9Kf1shEl%2Fhze5ixhphPPKMWkb4TXfZLVGDmTXF0SlmVha84AmSgXy6x4lBZnuox%2Bcuepl3HefO%2FUsbSYzbSS6KhlRePKQZze4H3CNV512LO9dQkP9dO275uygORkGP8sPWedEHL2nRfBZ8pRUOlie4DOtpRHdIN8I6arxnjPXh2yOmmLrQw4RGZRHXGKR1aDWUFmh0HCCmi%2BR1ywCBZE4kcK4eMMsF9k%2FCFunxYxbEvnvYrzODaBUzwEk4udpWhZstSoCHDmbpm2Semm%2FT8h8pBkVtzijO919ShnGC1Mp0o%2B9vZp2Xn9qHi485r%2FJE4ZB8XrF9JYycTbKFIGF%2BfweNvVJBH6p0oul7IBKdcXGkNPlEgOp7I7IL5jnu1Lq4b3HiM68mh8Kr24RCgeHZH5h495V78foqfEhYav8ZR5vc8uwpE9Q5AYYzV2HRy95KCuoxhNlD3N5%2FtxdTErVbJrkGTEqH9ZrfGQ0G%2BqMnf2wlvNzA7js5E6uBLmlG9zC14IzeXvRGr5iJkXyIMun92qTT6Y5yTFP%2By0Mei%2F8cba3P8eyLqrX25LKXYE57EftZPZW1Jvq0Tf3bTvzc63PjuhQ8CeIwkZSKvQY6pgHKQMnQETzWUlsLWZQwJP3uf9Z03GTvII9pbcuW4Bn12KPkKB4MDkSGTHm6mEYfE9KRdOlxI5B22mJEm69Nb%2B1U23VG68KA%2B20ldoZVA5B70phCvpv%2B34wXQaSpVls9TLltIROGzhP61coY0UtLiuLst1EYd1PCQXPt0O1R8HMEpC8OqLGSEm4LPTPWFCyxxX3eESA9vxJVYqwtRhAf2rklv1SmJ71a&X-Amz-Signature=6efcf2dd295896ddf76f1a296c7bde1d655d12336fdb1f12c89c0f34c267dfd3&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673G4MBFX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIAQJ8haFJCMPNjFRMh6rJDBD1h3m5L4is5SGRJFBh30HAiB1TQ4iLzfcO0GTMZPDEdSp307KWouog60vpm2XzjXsUSr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMAyWQeucaoqaRxm3UKtwDgKzE7xtQ6ycrm7bQlFAGQXG4hfYUjJRDgO9Kf1shEl%2Fhze5ixhphPPKMWkb4TXfZLVGDmTXF0SlmVha84AmSgXy6x4lBZnuox%2Bcuepl3HefO%2FUsbSYzbSS6KhlRePKQZze4H3CNV512LO9dQkP9dO275uygORkGP8sPWedEHL2nRfBZ8pRUOlie4DOtpRHdIN8I6arxnjPXh2yOmmLrQw4RGZRHXGKR1aDWUFmh0HCCmi%2BR1ywCBZE4kcK4eMMsF9k%2FCFunxYxbEvnvYrzODaBUzwEk4udpWhZstSoCHDmbpm2Semm%2FT8h8pBkVtzijO919ShnGC1Mp0o%2B9vZp2Xn9qHi485r%2FJE4ZB8XrF9JYycTbKFIGF%2BfweNvVJBH6p0oul7IBKdcXGkNPlEgOp7I7IL5jnu1Lq4b3HiM68mh8Kr24RCgeHZH5h495V78foqfEhYav8ZR5vc8uwpE9Q5AYYzV2HRy95KCuoxhNlD3N5%2FtxdTErVbJrkGTEqH9ZrfGQ0G%2BqMnf2wlvNzA7js5E6uBLmlG9zC14IzeXvRGr5iJkXyIMun92qTT6Y5yTFP%2By0Mei%2F8cba3P8eyLqrX25LKXYE57EftZPZW1Jvq0Tf3bTvzc63PjuhQ8CeIwkZSKvQY6pgHKQMnQETzWUlsLWZQwJP3uf9Z03GTvII9pbcuW4Bn12KPkKB4MDkSGTHm6mEYfE9KRdOlxI5B22mJEm69Nb%2B1U23VG68KA%2B20ldoZVA5B70phCvpv%2B34wXQaSpVls9TLltIROGzhP61coY0UtLiuLst1EYd1PCQXPt0O1R8HMEpC8OqLGSEm4LPTPWFCyxxX3eESA9vxJVYqwtRhAf2rklv1SmJ71a&X-Amz-Signature=01c7b65cfaa33544a5211b6520491653bcce3eafddde961f2de5fd9cafbf0e95&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664W7XTOWM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIFbXXSG2rC8FG%2FNLyfQ6S8wBN9H%2FBEEtCKAIp5hvP%2B8hAiAFJxKtpKdOnyxduwj237vm6q1%2FQ8Cnh%2FaAxqK5QiwIiyr%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMWasCRJVx%2B2hUpRmJKtwDJpJiNEdFvPTOWtFbM67QnASgv86UAAZQKvGFyTgxbmh0ScC3qIy59BLqpKFKHAB3MOKcHtWrakR1HiMo5o5CzppyYqw3INwffZ3Fj6brKZ%2FKvHoBGFnebkSFckGSEOP%2F7ddizdCJoAf5RAgggRq%2FhFqnbxPYcfCY7JkxkhGn8p6cgMxOt%2FR2JrCwtQvwxfa9vPpBvpNYWLFGLYXqLOzJRgcWwZPDTexkt4k8KRrJthKeaEp93rpRAA6RyJSnhbALeErqvTtImQC%2BfiRy09DxY7BGELXUgNuMczEMFML0M7n%2BxyCaGvih11sI79O%2BJqmtIJeT8Hoia%2F063NHgtAa0AJ1XmLokCVOUqteP6SU0m3QOLgSAAywIR8MmaK9HXwaVGtv5%2BWvcYfUQQ65dqsoRq5M1imQm1ZoIlloxAxBnL%2Fw2ahT7ZNOTdjIh5iZqxDyI5P4Rdf2KyEA39CMeFuqzam3ogajueOkEb5K6wMv58kLYo4pgyXAIAOvGKp0noNry3Ji%2FyUsTNkEGQG491NDrYqLSXHvsxfqn5atl%2BchhAH6Ok8ROMW6%2BkZg3xdxWej1cosp26XeXIwx7aIv3%2BIrOrLU1JacUGuU%2Bb%2B%2BQBoe3tKybn7EINf2XOvIR9Cswt5SKvQY6pgE5i9QWvpITdRfQC4qqCrF0gYWJtgGgMKdRSiByx4FeSH1WEK1oddd5ODKiDfVmGDWawdJd1U8zoIDmnyknsMPJI2xkLDmuq0oqoUbxvo00iLfLfl6qKe5KH1hq%2FpHadOzE3ngqw791WWIp1xvSnxnaCOg4bCP6qX56Pxy%2FHlh35P1grGIFSa9WVnfsAnZnvr%2BuvxYZgljwRXdXIKfKf0v7unBolXcG&X-Amz-Signature=3f9d21b36e5e64dfecff57c4306233db30719fdef07920989283cbf6da8c437d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLAKUCOG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQCQbPSLT%2B6IAHq%2FcIPVc2op6j6FY9C5ObPIE1buTfQYWQIhALu4z5WjUSYfJk8dKNf5W2dDSkjBgePBFvBkLb5V92sNKv8DCDcQABoMNjM3NDIzMTgzODA1IgzgUgYeuhJ8lm4dpjIq3AOA2CCbeCKLwakJkqHpGaqah2ri%2FcdI2GMIMLUh3%2BgPfzJ%2Bo98ZQTJX5J3fGzrNrB%2F89FfKNat55I5LeeAT9hCZkePH%2BxYmLV15eJgaIBAgoh%2Bu2TwmMBReICwAzeCRVkve7ipPe76tK0JxeSY7hnIOMmXMcJ1akh1pH2ZM3DJcsYp7NY4iofO58a4TQSsRLW8ALvs%2BdukcRSMt47DZkmRZSPie6iIJ%2FpNOijJTrgqYpUsgVIYgGZyAMSPLmmUxkqR2terR%2B20iCjfSf7qknb9JHWzSXX12mNNsDtPc7B9RX0b%2FolbfdpCjZjhzKloWkGE2RHNmMMA2zoHyPq%2BDKWqhcxhixwVw47TDwVWJKv4MEJsSWJ0IAoQX4haFIOQ8N09w3Bxoz85rUyDS%2FoFu5R5ODwKUBE8QAPu9O0nwo48lqajUx1%2FKZlNjAJHllvtY7MFWq0ii23UMpPQfZprOMJ5i28yv%2FebymKZZQBdWI6m2eUl1TT8UNdnWUcQc2AdMVkEJ5zGFxRa5sNVj%2BpM9dgH%2BJaEs8fzDjFKkWNdEk3K3luU3XjjE%2Fr3Nlwe7C9sguXqOvw2TfyCmyhdBP95PukzyKa6bEA%2FQ0UR4nC5dOqNFCiVcAYI2Ebeq%2BXmSTzCrlIq9BjqkAW597Q58J3JZxonKyZOOTHcxeSqUYpcQsaY8Dsbjnp6%2BZVZv5HVZT3PsyrspImdrLJAG0GAb9o1d%2Fu1C51EwnwhZ2qRsdFwEzoOL5Y0rE073vta2C9UQXg7xdf5IhLCx5zZ4TurSG9uPo985iHGBwP1B7iQVjMidwPsuNT0cfDQQmMHoSwyo93%2FpVhI2nlnON97p%2Bk%2FTgP%2FtHW0P%2FEvTwXV5GYAB&X-Amz-Signature=badebcc54bee62735d98c83369987b4957012eafe6fde2eff644771207fb310d&X-Amz-SignedHeaders=host&x-id=GetObject)
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