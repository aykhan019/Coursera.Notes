

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=189475200c702be2392a1a028622e8220083e70a467bf71137ca0f42dc0a41fd&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=9f4b93c4d999cedbfeba1850d7a10d34dbef7d9e87eb7f8f65121fbbf3eb99b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=dc68cde1d54879305701284454220ccbcf2c2b69486f5a4a1b0a2018e824b7e0&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=54488cec8eb44d8e64f5258c4971f70691d321a455eb35d02148a9055d62c6ef&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=f2261fdaf142c3595c52413b0b29d5a48c82b3318de418895a6bc848426f0372&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=c058b5462260841755ce0257fac279e0aeffe08edf0cddafff22f2911e28d771&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=eddb41dec2f118c860515be66b258527337e185f3d0597e51c55c183413b27df&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=9d28b19baf53f53ec261f02d80152ab97ce4ffdf9cf11290d6323c3a81322e6b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=be6d975b14d32d9fe29290ffff4422e42b7dd5e52f9da5c77803bca8c6474322&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFT5N42F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnw4ZlYipO%2B7CrWlOmgbXtq14tOBDGpySslcM58irstQIhAKzG6%2FwRBmnj0k%2FgSoxSSET1sT7vptd6JiBsTLVbSI6CKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXKU8Mmmx3Tc3lRFsq3APixi90KLxXSD0DAl9nWb4JJFMeGJxvIA8Hqg8ybylcP%2FjtXnBQy%2B5zJOB3rzOINJhQW%2BK8RkJtgP1cY1U6SjKZmLSHNulT4XK7DayD3fVhKTubcoBmnbI3Ux838sQxOoBNtwGMulPNO7lFZU4hT6h8M0bb0WHMiyvvJ8fNx0GF3tk1i8NIINvM7TQjj1DOPUoLESGLfgeyl%2Brqr%2FILSv3H%2BBHRuWUAhHSzX%2BPny1gJ%2F0J1QiXIaV%2Bz16knM%2BjL2BJecdcHaBsvfQTErXmvrIjmEOT3o2LMvtnQvPM5GLBZEAD9jIfWXuaJEI1HQWCVmoh3cC7Q9X2lwgxKxJerrlN5NL88cn6WUwqt5oIunLF1VMiEB232xpU7lpOLWLa7dDbfVvHJ96qY4V5c3InNUIDSawSiY6srpH5k9mfwFC3hgAbx%2F2mAEZxxgFMuzn67gubdPRkg%2BNkdrpi4H%2BGNZ%2FZx3fi05QWQt274x7pduUWeBEddK%2Fm%2BEiloYf4lKiJuITEkc6p%2FbTK6afad%2F0%2FdLY%2FmDoLx2QyomiKXvFwcFf%2B%2FrJADP6UsVHt4B5tMC%2FTQTXwLz4N8cd7gA%2B6O8jWc2LoXzUdlG59T5eN9vSJ4oDH34qaoLPnlKQgGiip1ETDGoOa8BjqkAcpH9baf3NTeZ7RnRtL%2Frc0mWkqPdMkQY2fCBTyRxU4Iz7Ho2krz1a3oJOxT4CFn5IMk0a%2F8rve1Gwl%2FMbdYhR5j7GU6FkPDyO3l7ovKh0ArM%2BNva8tGsJA4LHKmGX32JDR1gLR5Vr1de4qV1PIAhwfgsayaCXwCcfaX0p7lXz8Jppj%2FuBNxo%2B8lCZ0BKxigJu0j5ps3lvX41APiZi2hcuShz9dS&X-Amz-Signature=a4b1af978eea5bd8b6aafe76206babcd0077a2124d44e4dc955cdcf691866b33&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFT5N42F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnw4ZlYipO%2B7CrWlOmgbXtq14tOBDGpySslcM58irstQIhAKzG6%2FwRBmnj0k%2FgSoxSSET1sT7vptd6JiBsTLVbSI6CKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXKU8Mmmx3Tc3lRFsq3APixi90KLxXSD0DAl9nWb4JJFMeGJxvIA8Hqg8ybylcP%2FjtXnBQy%2B5zJOB3rzOINJhQW%2BK8RkJtgP1cY1U6SjKZmLSHNulT4XK7DayD3fVhKTubcoBmnbI3Ux838sQxOoBNtwGMulPNO7lFZU4hT6h8M0bb0WHMiyvvJ8fNx0GF3tk1i8NIINvM7TQjj1DOPUoLESGLfgeyl%2Brqr%2FILSv3H%2BBHRuWUAhHSzX%2BPny1gJ%2F0J1QiXIaV%2Bz16knM%2BjL2BJecdcHaBsvfQTErXmvrIjmEOT3o2LMvtnQvPM5GLBZEAD9jIfWXuaJEI1HQWCVmoh3cC7Q9X2lwgxKxJerrlN5NL88cn6WUwqt5oIunLF1VMiEB232xpU7lpOLWLa7dDbfVvHJ96qY4V5c3InNUIDSawSiY6srpH5k9mfwFC3hgAbx%2F2mAEZxxgFMuzn67gubdPRkg%2BNkdrpi4H%2BGNZ%2FZx3fi05QWQt274x7pduUWeBEddK%2Fm%2BEiloYf4lKiJuITEkc6p%2FbTK6afad%2F0%2FdLY%2FmDoLx2QyomiKXvFwcFf%2B%2FrJADP6UsVHt4B5tMC%2FTQTXwLz4N8cd7gA%2B6O8jWc2LoXzUdlG59T5eN9vSJ4oDH34qaoLPnlKQgGiip1ETDGoOa8BjqkAcpH9baf3NTeZ7RnRtL%2Frc0mWkqPdMkQY2fCBTyRxU4Iz7Ho2krz1a3oJOxT4CFn5IMk0a%2F8rve1Gwl%2FMbdYhR5j7GU6FkPDyO3l7ovKh0ArM%2BNva8tGsJA4LHKmGX32JDR1gLR5Vr1de4qV1PIAhwfgsayaCXwCcfaX0p7lXz8Jppj%2FuBNxo%2B8lCZ0BKxigJu0j5ps3lvX41APiZi2hcuShz9dS&X-Amz-Signature=3db4bdfd9628d5e9dd44a4c5d976b7b47134a365c5b2f19c6c38fd2c4b70df64&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFT5N42F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnw4ZlYipO%2B7CrWlOmgbXtq14tOBDGpySslcM58irstQIhAKzG6%2FwRBmnj0k%2FgSoxSSET1sT7vptd6JiBsTLVbSI6CKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXKU8Mmmx3Tc3lRFsq3APixi90KLxXSD0DAl9nWb4JJFMeGJxvIA8Hqg8ybylcP%2FjtXnBQy%2B5zJOB3rzOINJhQW%2BK8RkJtgP1cY1U6SjKZmLSHNulT4XK7DayD3fVhKTubcoBmnbI3Ux838sQxOoBNtwGMulPNO7lFZU4hT6h8M0bb0WHMiyvvJ8fNx0GF3tk1i8NIINvM7TQjj1DOPUoLESGLfgeyl%2Brqr%2FILSv3H%2BBHRuWUAhHSzX%2BPny1gJ%2F0J1QiXIaV%2Bz16knM%2BjL2BJecdcHaBsvfQTErXmvrIjmEOT3o2LMvtnQvPM5GLBZEAD9jIfWXuaJEI1HQWCVmoh3cC7Q9X2lwgxKxJerrlN5NL88cn6WUwqt5oIunLF1VMiEB232xpU7lpOLWLa7dDbfVvHJ96qY4V5c3InNUIDSawSiY6srpH5k9mfwFC3hgAbx%2F2mAEZxxgFMuzn67gubdPRkg%2BNkdrpi4H%2BGNZ%2FZx3fi05QWQt274x7pduUWeBEddK%2Fm%2BEiloYf4lKiJuITEkc6p%2FbTK6afad%2F0%2FdLY%2FmDoLx2QyomiKXvFwcFf%2B%2FrJADP6UsVHt4B5tMC%2FTQTXwLz4N8cd7gA%2B6O8jWc2LoXzUdlG59T5eN9vSJ4oDH34qaoLPnlKQgGiip1ETDGoOa8BjqkAcpH9baf3NTeZ7RnRtL%2Frc0mWkqPdMkQY2fCBTyRxU4Iz7Ho2krz1a3oJOxT4CFn5IMk0a%2F8rve1Gwl%2FMbdYhR5j7GU6FkPDyO3l7ovKh0ArM%2BNva8tGsJA4LHKmGX32JDR1gLR5Vr1de4qV1PIAhwfgsayaCXwCcfaX0p7lXz8Jppj%2FuBNxo%2B8lCZ0BKxigJu0j5ps3lvX41APiZi2hcuShz9dS&X-Amz-Signature=bf4934e179f32e50a131377d0abdce21db0fee7620ff1fb1af95e2f9a5e3d7a3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=fdf518ac6ab5a655738de08606eba6ebe770bcc32ce71c74148b975bb4c5bf58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=53661c3f9cac28b027fc2284e336e61bc52ac1db13fa80d77955551d883a20d7&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=f2c1462f0aa9ffed7c02a0d7d50e20e87680210f787a77a078fe352d146ea980&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=266a83da659b832f0b9e789036dbd8f11ca6d3a6424fe239b24cf2a143a079fb&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=013c39624a0ccc8c72ab728394f52b5f5a01334608dbf8c2b8bbb08ed1b1d3e9&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UP4NZ3C%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIDRnq2Lqi55dd53O%2BTqHGP1LSa3lPN3yWsPIJs%2FYEf8SAiAsvE3m%2BX37q3DrP16xGJxukL6xRP%2BFPJvUjOcYlmjjuiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXAixyXLwB9rXLdefKtwD22R3Cx8ZNvsDhRoHHn649ohfq4Hm5XW4t2RkmCkfWADvhwE%2BJsb5yA%2BPuRlyQu%2B3ez375Jg2QwCrEAwXBn6m3w4Y2vGUS9mRqhtCIXyysrChr6VdPaZIjFAYGQWnWb8HaJK3WOc8eko1yUM8zhFFhjP%2Fsyk%2BUIYMQ6vN2VzFIUjJbuyEh37akl%2F2J3NTVLxteYdJLpVFss8XOBu%2BhpFO%2FuK9iLmGVema%2FfULswusklLcJzRgFyaCqZ3GBddntRZnglrxrkMZ0D3mNaXTpd8iNIxX1miGjvzf1h6GHCJAZ4zbvTHSPbDxAbqoBc6FA5r88yRiGtTGVt6khqlF66bCvD31%2FbHWtfFvyCHyQV%2FnSiJfy4L01mr9HdE0NLyNIPI%2BgUaCSDKiaJukFQu42%2B8VROC7pqEEoQQxgbduVswNHgPRSuFwtZsUvBLlHAuzC2lHQe%2BO34rzu9qcUjGMZiGVh7DRSzAszNYY4P%2FpazB6qsr9th3SuW2P%2B4O%2FUW3Ki1JFvn%2BMK4PflaqyGT%2BAxZeoyHSOGTUvQEa2GnoDpXUBbb3G5FmaMwFfDQMzZ0KKkg7d%2F0xF%2B%2BYraqU%2FXU7kCD3JQLPNxIAKMmIrc1%2FCB2zXHUAi9%2FTmdaE5FH%2B7VgAwpJ%2FmvAY6pgHFLNeffPxL7CwLjeu9M86yk7msfEQEiO0sZz01eYb9U9ivXrW4aO%2BY3ksoDLxsOidnXwlCglrSRYjjdloLC1GpknJoq6To3VVZntlUoRpsi8PffmsIOjsq3MfeKHqk1VBMPvox7syPmysyIQy3%2FA7HsgTuVXLY6ERWCKg4M1K64QyK3A29YGqBHF%2FZlRiccy7JMVK3tKtPC08dSsUzJu7pkvehJOZU&X-Amz-Signature=734ea197b1a331410c3fffe91ba6ee6516915fd6d6e2f53153d38343af1a8481&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=7c891c9b351f9981e95ba90ff0e457db42db995f24a91f9e0d2a473bc8b4071b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KGXMCFY%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDcaHDqYwon1NhizC0AFR%2F2PlHiEadkJpjPf%2FTD%2FYIkgAiEAlPKYy58huZSOwnM5hT1wyYASRgdGGwM0cWhGsqQ8Z5MqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE6FQTlGAUmg3C8K6CrcA4LyGrmcMdUXWMubqnuWcSaaNn9bDbqcHeaPNd1YP3iI%2BA9Bln7Scrhfw0mkjtjGJ8MkcexmXhuKGzZkDBPdAURUw%2FMO1xufuJSseUJSz9m%2FsNw7F1VwHrRwdEXW4x2uJowb5x3LYqmXlKVOeC4Z5W82u%2FJAiW3H188xmCyuEBKju96XphZCSqTw0ntVzyDO0tRVShAe9fi6HJBLTzWIu9SMkayRK%2FZ2UntOKXJq%2B41RolHuzaO5R%2BOQ%2FMKKJoOEtBeTlCzIjha%2FZ6A8p4EHuP4OipJRpZrFfGB9wrBOKzZtSRLVpE9iMt5vxsdOdytbUdPjsm2F8gqTrkHt3nVEF7HL1M3RYvBs9isI6qh9VXLhIDQGJPs8iSD35abUGZa8BApQlPgt0txpQM877PIaw4leu6QTrdPTAgmkXF9tYcvpkvwqXHm4l52H%2Bzifc1qzEAcZGMMi96cvs9NLWZx%2BUNkgfkPVFKiY4Wvo0E4CMZOKPu3SYDrmi8eUZStIi%2FYSfbMBfmCUU52KWM4y7C9R8EUlVcaz5YEaOLxFVEYUn0Jc832HWG3GYEcnuRQZRE01BjG3JwqJWpxJwTCHP1pq0WMcS1H4i2s42KrtIhmjKmsyIBLUZ61KRGUaC1VwMIKg5rwGOqUBleOS90WoW092QnvNeyrufu8nzXvAqiGVova95iIJpVB%2BrevjVNZ4I4uVbL5j9wIdmrpIPC196kNsD0ERHD0n%2F0JEJZAINdiPhRnDW8712P%2FxZJtTwxLdPk8t3ylJVmtkqVqL3eR8O%2BXIkDh51zXZbksaUs1gCJlocFWmP53d0r%2FBiANWs57A%2B%2BjlnBU7BuvUr7EE3jmCSEsahMw9vaoxfE4cwH7a&X-Amz-Signature=4cbd0849c9ff04c0ce7e05d2ad5901c6e3e8818ae871d495640e50daa26b357a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X47TTNZR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQCxWD9kWmmbsO9Ew9Cx9M%2F6LaXZjQaWfGCGQgOlJj9lsQIgIJDSLJU8IrCQIlAN2g8n2m1%2FpxAqGOCX9vqM849qARIqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMTZE58EwfPlDve6DircA2ZOyArb8eisfLhmdRoag9StNc707%2B1FS8oXQLzqGXWA6JiCZS1C7fQQehzMhAdgyiAT6rK2s8eu1xWXHLnbDTEoCDoWp0t2wvWJusMQjoIPuVgPaoLzwsajyUytdwK4c5qAdB92NweGQ1ESAZDd48KOBLkTWfiG9FJmQqdkWX%2BfzgmQ5%2BCMV64blbJCN1oOKT06UfV%2BmLHmUcFEcAtterMiCWkv0cqhhIHRgzW2UHJ1C%2Frvgn%2BDcxy2x%2F6AgPIW%2BTzAXvolYNc7724wN%2FzuzkSNAXLFSASHjhC9GYIIt9VQk9ix6GoGV7Spsh5kOcKI%2B4zZZy399iAuxUnlozGpx2tRQAAHd6KbWg9S6n6fXijyFURUm5NRxLF8JxV5AHCdORMyXF6Gf42TkrdDW03Tzrh5bV3wyHRHsIQbINcLPj5T8LjJ8%2B1OOzjOQ4D%2FmIeE3pMvwz%2BhCNYuO23TtON1Bdg%2Bg0UoQZFM7T%2FSPvwQL%2FJsEV3dV6MIj1%2FIXo1OFCbQiZ5imIaxruYBtAJFuY%2FD7H%2FqLgk48Zo%2FCUEkNUD8QecTxRHdHp4QpT5G1dfi4%2FIDdayE8Cl0WQW6A4anZwq%2BFrkEVLc4910MS0gHqsLFoBA4%2FKGG%2B8zUwWA1ccXYMMGf5rwGOqUB0KD20ISBDp2YrBtTGxsR2hAVrXyubYTkd4Y3XMFztquakLy%2BTR0uG491mbf4sidWjC3%2Fm%2FaF3LgmmIn%2BCdsuSFk8j4H3hzsv1xMQqo8Txb42s3Xnf9jABBZteKVPOqyq%2Fnqv1obYjJPG5AF0Y%2B4pGGScVAsSSQSjV3e6d2BTHl07DhpJGKtwjwz%2BG8wthKVFi4bZTEJJr0wuIYi2HdKtcAzEgHYK&X-Amz-Signature=35201dbf7a0d3115b6d9d637800515e4cd550c791e6851997ef4e930c558b8f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCPWATD%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T024031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCJ3%2BUc4O19x5SpEA5N%2B5Uv%2BsK1T6U07x2n1KoqHeerjwIhAOy0Yla3GKH4Xf6XrcqbiZnG02Ta6qIQTd5wo1UpW1oYKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5u%2FoyjP7r9y%2Bl%2F9Uq3AONhB2Ykhi011A3S08lN%2F3M4uq6GIoD4SRMJSMnfWA%2FAFsi6Nj50EnBGrmOwRAzeogjAoqv2bQYpQI06dz1p6ehH1sQELYA2Rc6kkGIJSnKOccqSlL%2FM0ne83qFZtYRNDDcqE6i9Kf7Buso8UwggqVtgasPqwPphzuKWc9eMuZe%2B7cP5jVY1zlgL4ZW9J9sjJtf4qhC%2BhXZnE2I7rEpJYwmMOKDdSVI6hQcX0RBlDBZxCNDdLJoMyrSYIu9aPNuV45aVYTYN1XVjDT%2FEux%2B6%2F0P%2BpLPZpqaMfVSyvK%2BBCKP9xq5kbkEmaG33earkzW9Om5WanFbMbiRdAE7rJXeCAwdYXlmvWWeQVvKubQlZoTRuRDcQYvDykVVJ8csqaA5bBm09UZ5xOmWf3HUWHWf7n5YqZam7M8zfeepmhhIWBti%2BzTLC8XMYAFLZALMqKZLtDpfWurWWbMfn%2FSgQQ2BVGUQzTRdAaT2KibTEa0meV9uhThTmZL6MWIDbxakZNl8CR8gqOhLaL4nOljL%2BesarY2NIpGKioc25IQu1c5Fe8t%2BMjF19q2hMqNVVmuE63mBlUC4VQjLJe7qUHimcCgalvpC4tZcvPsYIyB1DMEXsp7UAUIWfFrHBPGffD4F8TDqn%2Ba8BjqkAUaz77C1vFPyhgzaTA9P5YnB1Ay6NN0FE9%2Bt0mANWSuu5Ad8O7hQYY7ADA6GZfIoFhSBPlDHREXQUKg7coLN%2F5wX6FfzuOPumYYICGiJkHhfqocRT8bI6KHXt21MOZSJkT8pN9d4wZhr%2Bd6wcBqVCjZMpcSaPWNpzHFWpJ4B213Dj%2BymJb%2B1wJIMoKUzgd3nFAPsrdmGsTRI7DItPKV%2F1Ta5kG9E&X-Amz-Signature=69a30b4e264b519435a4172d174296ff892fecc280e52ee84a6cff6f0f869cbd&X-Amz-SignedHeaders=host&x-id=GetObject)
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