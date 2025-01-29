

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=b5d8dd230db9cdd22df0e675041fed82d2bf5f0459f73ec41f6774eee50fa096&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=f7cd7749a553d501867466784c53fe7f504b5919156f4a5e3794fe88eb64d2d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=5bf08e1ef56be36a24901863eacfca7f0d387af5ad32e0e39e4646219fe60e6c&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=5038e174143ba630b9f4e0ff6c36a03a1d2afbe68b15fa6daea1d87f03ac04d6&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=5093fd7e4187018269ca9afce1438df5f7dc966b9d918efc74a5915cc369f679&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=a59f41257c29d66cd22d644b46224e80230b330840f95c260646f4219bc83d91&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=c7e96cca5ecd39fb422d9a97c35afa8fb0568929a48d0dc3384fe43886b2dc0c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=c17204bd3b5161ba3da30ff15b047a4243ad67c3dc0410a73dab7e953e6f8785&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=14776f7c2acbe7ada07025cf718dd66a27de427fa93c2e730845b56660a7f8ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSXIXIU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFHEIsAmoUaU%2FaMXX7CH552M00fQSul03T4TVWadSPmWAiEAm2lthgTV13MdbZjR4wKojG6krVmz1%2BbFF6GsbhmYV0sqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHWS%2F6ThZ%2FwNuYKZIircA1fuP9IKQGIt5zS4BfxrAjMkF71wWK8cTANcZ7yw%2BKIIPL9MBflsGgdTiliTUdjixcW2M1%2Fu3XXwaep%2BTJNTv7XSSdRwzthwZO7S6QHDKH7pxD7ZogN%2FILaLEprfjXQ7t5dY6tDt0MUGbZwqciJ%2BP2L8kLX5Anht6EoGczRok3ood1ZLwHlp9rhfvY8CRWMXi6%2F9U9DFnr%2Fk%2Ft3n3HmLvF34i7MovzPOIM2jIlqDqS3lURcYyBnmGvGlQXNipuBxtK9OtxsEZA7LKwBpZRkSJl6WrSzOLG%2B7O3gTzTvJawjqA8mNTMXdcjKa87NkyCzr7a0zr0YsO0kiAJunUTQEfE8wLHNuD8729DRPs6LisDMfUUmY87ES3tpCjWYjIKBaGWxO0nZF%2FqBVgn0av4Rn5m1a3%2BqkiomqWgefDdnXkkSKcDj0m79bG80eMl1xnchzhtgR1%2FGfloY%2B0JXS1HXI4y6jNN19iDI8gsKfNC0WZgDf9TaqmO0cEiQFaOKKW%2BtTipWZ9gF9Lgf0oqn3jtToQ37NS2O%2Bcu%2BmlNOFGr91lhYY%2BTf4aNtneks7D95%2FHp%2FuXrSH72QAROU7VN5uH6mz%2BInChexmnYigftUlkJFz9qwBpmMsrmaw9FeJ4xNSMPSf5rwGOqUBRrd3jj%2BYQD2R8fng5FCw7OaNUJh%2B0MHuoewOktvOGODccvPEZejHIopFIDUbfSB5wro6mcdmwKPakYTfh0rWO2JO91z5YyAMy5E%2FuqCUocxCo909mN0tT7zVjibfj6vOyp0I%2FoJTU0B1wiYzw3I%2BzvlldOLUBuigUWZ6FTMN7k6xAQw09QQgEUYh5rOBmzdY0gXL4%2BS7Kp8q8jlWLias0kDj9QPB&X-Amz-Signature=e40972a40a09d045770594f1a7b5ef468c4c2f641ad4bb5fd24dc3f780556863&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSXIXIU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFHEIsAmoUaU%2FaMXX7CH552M00fQSul03T4TVWadSPmWAiEAm2lthgTV13MdbZjR4wKojG6krVmz1%2BbFF6GsbhmYV0sqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHWS%2F6ThZ%2FwNuYKZIircA1fuP9IKQGIt5zS4BfxrAjMkF71wWK8cTANcZ7yw%2BKIIPL9MBflsGgdTiliTUdjixcW2M1%2Fu3XXwaep%2BTJNTv7XSSdRwzthwZO7S6QHDKH7pxD7ZogN%2FILaLEprfjXQ7t5dY6tDt0MUGbZwqciJ%2BP2L8kLX5Anht6EoGczRok3ood1ZLwHlp9rhfvY8CRWMXi6%2F9U9DFnr%2Fk%2Ft3n3HmLvF34i7MovzPOIM2jIlqDqS3lURcYyBnmGvGlQXNipuBxtK9OtxsEZA7LKwBpZRkSJl6WrSzOLG%2B7O3gTzTvJawjqA8mNTMXdcjKa87NkyCzr7a0zr0YsO0kiAJunUTQEfE8wLHNuD8729DRPs6LisDMfUUmY87ES3tpCjWYjIKBaGWxO0nZF%2FqBVgn0av4Rn5m1a3%2BqkiomqWgefDdnXkkSKcDj0m79bG80eMl1xnchzhtgR1%2FGfloY%2B0JXS1HXI4y6jNN19iDI8gsKfNC0WZgDf9TaqmO0cEiQFaOKKW%2BtTipWZ9gF9Lgf0oqn3jtToQ37NS2O%2Bcu%2BmlNOFGr91lhYY%2BTf4aNtneks7D95%2FHp%2FuXrSH72QAROU7VN5uH6mz%2BInChexmnYigftUlkJFz9qwBpmMsrmaw9FeJ4xNSMPSf5rwGOqUBRrd3jj%2BYQD2R8fng5FCw7OaNUJh%2B0MHuoewOktvOGODccvPEZejHIopFIDUbfSB5wro6mcdmwKPakYTfh0rWO2JO91z5YyAMy5E%2FuqCUocxCo909mN0tT7zVjibfj6vOyp0I%2FoJTU0B1wiYzw3I%2BzvlldOLUBuigUWZ6FTMN7k6xAQw09QQgEUYh5rOBmzdY0gXL4%2BS7Kp8q8jlWLias0kDj9QPB&X-Amz-Signature=8dea43fbf583d39f8abea6621e8620d5b00bdde6e745f494b7aa186f302856f1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWSXIXIU%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIFHEIsAmoUaU%2FaMXX7CH552M00fQSul03T4TVWadSPmWAiEAm2lthgTV13MdbZjR4wKojG6krVmz1%2BbFF6GsbhmYV0sqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHWS%2F6ThZ%2FwNuYKZIircA1fuP9IKQGIt5zS4BfxrAjMkF71wWK8cTANcZ7yw%2BKIIPL9MBflsGgdTiliTUdjixcW2M1%2Fu3XXwaep%2BTJNTv7XSSdRwzthwZO7S6QHDKH7pxD7ZogN%2FILaLEprfjXQ7t5dY6tDt0MUGbZwqciJ%2BP2L8kLX5Anht6EoGczRok3ood1ZLwHlp9rhfvY8CRWMXi6%2F9U9DFnr%2Fk%2Ft3n3HmLvF34i7MovzPOIM2jIlqDqS3lURcYyBnmGvGlQXNipuBxtK9OtxsEZA7LKwBpZRkSJl6WrSzOLG%2B7O3gTzTvJawjqA8mNTMXdcjKa87NkyCzr7a0zr0YsO0kiAJunUTQEfE8wLHNuD8729DRPs6LisDMfUUmY87ES3tpCjWYjIKBaGWxO0nZF%2FqBVgn0av4Rn5m1a3%2BqkiomqWgefDdnXkkSKcDj0m79bG80eMl1xnchzhtgR1%2FGfloY%2B0JXS1HXI4y6jNN19iDI8gsKfNC0WZgDf9TaqmO0cEiQFaOKKW%2BtTipWZ9gF9Lgf0oqn3jtToQ37NS2O%2Bcu%2BmlNOFGr91lhYY%2BTf4aNtneks7D95%2FHp%2FuXrSH72QAROU7VN5uH6mz%2BInChexmnYigftUlkJFz9qwBpmMsrmaw9FeJ4xNSMPSf5rwGOqUBRrd3jj%2BYQD2R8fng5FCw7OaNUJh%2B0MHuoewOktvOGODccvPEZejHIopFIDUbfSB5wro6mcdmwKPakYTfh0rWO2JO91z5YyAMy5E%2FuqCUocxCo909mN0tT7zVjibfj6vOyp0I%2FoJTU0B1wiYzw3I%2BzvlldOLUBuigUWZ6FTMN7k6xAQw09QQgEUYh5rOBmzdY0gXL4%2BS7Kp8q8jlWLias0kDj9QPB&X-Amz-Signature=738e365781371dab6a5c3b2f12093cf9776c206de12cc17c136dc313d75e5d68&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=86a08e7fc799ac73486c48fdb4dc92b4a3c2f03cd6bb7cf83c911377e910edad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=46063fe0df4a6f95ca9ca6dfcbe42c8bf9926ea6df64cbc8f91a2666cfe9f386&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=8eabc760cbc2a7aee7695f1118cf81779fb1270d66f1f83bc9746c4108d681f4&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=e7679d132a8bb80a71017ed5a0018e15fdcd9b5940d08dc999d9cabfb643e2c5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=533da94251c1813d3a12756e55c2ae7996d3ee6d051f000991b5ece5e1107cb4&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKIYIIWK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIDic3Xjt1Rj49IX34nJewt3eZGa9QGnMkynZdajqJ%2BezAiApG7%2BWNbeX56jVaQ8fOzgzmFHOOecUSh0xjMNAWdsZbiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2M%2BEgNxIDiR138eOKtwDzbRKiix5vRtQkhT4nVb2PT2D9n%2Br0JNOiO%2BXbiRR7cOde81rKTu%2BLyxojEluMjzwzd6pZLLgKrwqDDCrbvHwDHvfR66V6rHw2Mh6a1JDMKcoM4tVMPjQL1fWykH2gbUrB8M3KE8nQiVVPy9KId0pJwUWrYN2Uj0odlDwjdiyq%2BgQsWA%2FhpGbBzqvohirWuy6BLg1xX14rdExpH%2FGi4ZUu%2FrkHvomnmlPOoroN3Dy9gnmrNUgKXfloVuhxCaw%2BsITAcCcu3hNZZ6ULCSzihGsqisSSt8zMc9FRVae1kah4yVRjUxyT3kE0XIpOXlSGXjINAtL2h0SPqxSOKXM2I3RyBYqSNiWZSQgv%2BtaQMvewbp3cAd8%2FUHhrsV7ZHpf%2Bo3TPlHzpUw6bJW5FhEIlVL6MorRjuWULULmKimjqIpFcDgUS0X6dswRZZLz3MTMmNRmTM%2BXYfTv7%2F1%2FC1g7GWmyUlE9g25Jbz4svCGzVWifcLA7%2FdkiwoST2hIRcu%2B93FOU%2FVixVbODGttwBU6KrTrBGGX8loMz%2FeyLLuCiQ21KxsEJhB7UtYtGARinAcxtyFpahtE9bLoYkXCRGp%2BwlzZYkG8fKqIgnK0Z7DayEtvYf%2B6wpnd42mys6xqJT4kwgKDmvAY6pgFjl%2F6QSmA37P8l5WenHPrsQmno9JQl5%2B6nOWurlIUvv3149rxsdKbQKwrG1lQeNucI%2FQCUk5McUFiuHO1D7w85j6Gup1DoxSQhnHRVIcIp4P0aIm%2B0VZQhrSmPpZFFjpKxUM3jJU0CN86F0pnLWCI%2FvTQC23y29zEDce5v5xSO%2BsT4WGxR6Ux60F0Ns%2BSxRPdE%2BrIUY39rrSQ%2Fe4IUJANTMytSPLWm&X-Amz-Signature=ead02c7afd31b5cd89fc1145bfd83e7af2a53d993a89147c43d50b90bf7641c2&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ZRZQ2I%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGj5wYbX1YnSR1KW6RYInB%2BJV%2FtlOKIlT%2F2MyC2FWKbTAiAQ4a%2Fqazoqgz%2Bdvn6QRyTvjOLu9eI%2B8TUbQ1AaDu%2FA5CqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKYuOGvTmqDZjdWJHKtwD5047fBuGgYQapyknnNr0XOK22l70oZITHBlM%2Fiy%2FSNGVMHCgLnVoPwA3TN%2BrOUnCdEfaupAs6gOuliJMGlRP7BsNZ%2Bld0TKgLIsTPzCJyVN%2BfrKBmrWgidwJ3CMhZGh9OcwZpZBp2ICkYUeeZjtBAdbr%2BZN4z4GvRKVoqMXW2W5eJnnAkB%2BHMVWWXoMnd0QN1Rno2YhnhstkiG5AxkA%2BdnzN%2BWJWcPi64laRQWSw4HmeQwKA3DK64Xe7xu%2Bk0xAKbEM5SVMyOA8hiOPY7bo6xc6B1rN0zs%2FS1UNx0Nxas3Sg%2FqvkNQ7nm4i7B16ttO4y6wejOpm7HN%2Fx%2F7CCN6esIBR5yCakRjvDmBBepB%2B90UP53YFK1H%2FikZLxLFGOsUpleoKTSSlGe3Y4IFTfc8zXkyyQh%2BdjChAJ1kf0DwLgW6oPCWZMV3UyVwEC6KygglmW8nR1s4UoAcAJSVlkzEJ8ArbcGaHOa1Ota9WPUKyYDML%2FS%2FGuL9ZfGcN6zgcvUMqgsn%2BBpfzHjzRNVoEyl19kPselQxiyWsXlov86pGQdU0amcl4%2BV%2FmkOljz7HeMNpNZhlCIx715XPCB84qfikyFaqwKxEHZZRB6c7bg%2BQwmSZlMIlTabrj9vGYc1eYwxKDmvAY6pgFuNT1C4YjMUNC87Valxcv1cneJdvI6yo0qnF2UMXddzJ6bx8S8clXkpLD1K21mkBPNgiGYw5G3gIs9amcYpf9l0XjzOnhKCacrIRU1rhHtbgwxDK5ORV4yE%2F1gvrZKZm9dGx0nWffzabdsg6yrx%2BpaUFT0F422OrcoiT8TOi%2Ffx3dBrvOJPgWUMc4C0hExDuovpexKV5HdwXLJRLnNBSsUugX7Ktdu&X-Amz-Signature=e24de8506a109b980fe58d6cb53376d2b19e6e52c5c16e4496993751e9a66755&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4ZRZQ2I%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGj5wYbX1YnSR1KW6RYInB%2BJV%2FtlOKIlT%2F2MyC2FWKbTAiAQ4a%2Fqazoqgz%2Bdvn6QRyTvjOLu9eI%2B8TUbQ1AaDu%2FA5CqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKYuOGvTmqDZjdWJHKtwD5047fBuGgYQapyknnNr0XOK22l70oZITHBlM%2Fiy%2FSNGVMHCgLnVoPwA3TN%2BrOUnCdEfaupAs6gOuliJMGlRP7BsNZ%2Bld0TKgLIsTPzCJyVN%2BfrKBmrWgidwJ3CMhZGh9OcwZpZBp2ICkYUeeZjtBAdbr%2BZN4z4GvRKVoqMXW2W5eJnnAkB%2BHMVWWXoMnd0QN1Rno2YhnhstkiG5AxkA%2BdnzN%2BWJWcPi64laRQWSw4HmeQwKA3DK64Xe7xu%2Bk0xAKbEM5SVMyOA8hiOPY7bo6xc6B1rN0zs%2FS1UNx0Nxas3Sg%2FqvkNQ7nm4i7B16ttO4y6wejOpm7HN%2Fx%2F7CCN6esIBR5yCakRjvDmBBepB%2B90UP53YFK1H%2FikZLxLFGOsUpleoKTSSlGe3Y4IFTfc8zXkyyQh%2BdjChAJ1kf0DwLgW6oPCWZMV3UyVwEC6KygglmW8nR1s4UoAcAJSVlkzEJ8ArbcGaHOa1Ota9WPUKyYDML%2FS%2FGuL9ZfGcN6zgcvUMqgsn%2BBpfzHjzRNVoEyl19kPselQxiyWsXlov86pGQdU0amcl4%2BV%2FmkOljz7HeMNpNZhlCIx715XPCB84qfikyFaqwKxEHZZRB6c7bg%2BQwmSZlMIlTabrj9vGYc1eYwxKDmvAY6pgFuNT1C4YjMUNC87Valxcv1cneJdvI6yo0qnF2UMXddzJ6bx8S8clXkpLD1K21mkBPNgiGYw5G3gIs9amcYpf9l0XjzOnhKCacrIRU1rhHtbgwxDK5ORV4yE%2F1gvrZKZm9dGx0nWffzabdsg6yrx%2BpaUFT0F422OrcoiT8TOi%2Ffx3dBrvOJPgWUMc4C0hExDuovpexKV5HdwXLJRLnNBSsUugX7Ktdu&X-Amz-Signature=55146e6939dd59c2848ba8c46eb0def017a3dc02232f25281d0d6f9a0112ad78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNFIH3E7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDNN6mFPFryp7C4%2Bup9wn6521JeD%2FZ0klMYSbAlSUhUSAIgbYEAGfLSMuMxcPifScthuHU9AN%2BNorDZxi8vykX1uvcqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCGAqy%2FKeGH3M%2F0zSrcA0OC1Ipt31yfWcoxu43eFFb4TvKh%2FiLTKvC%2Fq1GoMcsz9HZOalRd%2FI5DOnw76tw5sCsyW9UZW9O1XPeu1%2FWGlJVf3jOAWGIorHntqZSBKC0eTOyfuC%2BjNLwqaZnYBM8F0gN4C3FA7kI%2BvNehTE1bvJ9g5%2BKLDVUWikga%2BdNsvYYfEYQRVl6Wkfyv7Y13PkmuGoM%2Fmye2LcMc%2Bm9DcViLdPQNNCwLKGbAEyWXnC3l2fOKX4Eg8M%2F5fx0lReFkgBdC9Tw27mqn6XNtJ%2FAA7QQlhG0oy9F6sBsIqgMOUfuv45beybjbP%2BgcOTQcigZdMFw8e%2FzWXpTaNNBeFP1RmRTnv3KSGC%2FCV1ByOILlrHFobDcjaTpg4RoxcRfYN7hEdk1p2Ni2bB9Yg8UpGtytpRwntdyre1bsTd0ODBotTfiP7jix7h%2B5fWFZNLPZkHxy6Xeo23z5qyp84wrpFEQNZiNzBUk8msfCE%2B94ITc37EtpFxfDihTQEY1OHFYuGVC2vrN7uwA4cgfzf1kcxx74U0MFHM8mzpSOmzjMY2DPgWdYuHaAUXf1zaE9MY273TIwzG2hnNta5IqlPFEiKVFcr6vIUiligG%2FthhO1KiD4CFGtnuBp75OF37Pm5lOuOybmMNqf5rwGOqUBh%2BS4kMOwiQbfb4tZK07zc6eKgMLm4w2ZKjvIKwjHk2mPuX3LKevC8Zs6gavz5GVZHJNiXbVQvgdLACRHyc96wo9Dwz275A7SD1pZnw7yaJWUeZi1iVStdphSM6Tlgi6W7cvClXBX2I3uwUcX00iFXWEXemBH2mc39MrKNKCbUTGMYTm7j8x1fzx%2BQpYDh%2B17BetW6Q%2B6JDLQO9NnSC5In09EQjGD&X-Amz-Signature=dd77ada7d9d493579612d7381c8febca4ce0dedaa04d2f63912688bc13af5b2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJD3YNK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIB0P1ZLs7LFuPuhH%2F9r9UH4cWH1ZOei1lKnYswAq84E4AiAa6vgUV0nLsFGud3h0TabOZAokJ6SVMxHtme1mDYcRhiqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNdhcciocU3qPrCasKtwD%2BhTQSzFt5%2Bnys9TH86KXqBQPQIRl1c9V2oqxwxzUp8JBGDda9r5zkKtVrJI0Xb25PBnYb9MuwRmz3k2yo7oHUDdgT2uA6%2BGmpvBQ5HHBnshzNIN%2F%2FBVLollD0iBq%2BaRA2sbGWvF1wsqAI52yz%2FmxvLVNPzwU51rYuRjjfQf9iKePhnVnZeviuGgaV1Y1cgcwQEokl0VbXm6r8pk6fiy4NRhCgpGBEYMxP16IByspS6mPkxGhNHApU%2FN3%2FhlnnZXuqS8r86l6c5%2Bx%2BSVgFAGw3z2JmxqnGtxphTqW21TkrsHzeManhpm4gkj7m3kA%2Bn2vK4fjRdGLV4xmSaAH4iluwxVL3RZldU2BLmnB0plk5GY9F%2FBfVfmiqt%2Bl%2FEPFOtZqpmqwJCxoyJx0nQ1xDW%2Bd6BdEdeLlYqXVsDuTAaGyhsQUz0CWpYe2iSHabqrg%2B3RFzpE4qVkjRYv%2Bgs%2FV1GulNtbLC%2FM95Jh23WcqBbl4fOmASI%2F4sfxmTfJHGR18irAP7QfrcR%2B6JG3BUOmgXuFNMgWC6DmSZe8xk%2B%2FAXFmBLUkGOuVkdZ%2FLbFmJ1xHexrdjNytPPaWhrZVjAOGKwo1CFT3UqPhzn8NbrbOeM37pJzqIaZUaxzJ6Obw%2FrGIwvp%2FmvAY6pgFrroiFn36bs6ESGzIFSyNakKSWQpqxyu6br4yq%2Bx6basmcXJTkU%2Bi9Bg19m8T9g6PlHZPvnL318YRWA33hCKBK%2FD94X5eXFK%2Fw0C3WWj7og2tv%2Fy1qOYyEodjF0Jzdl71U0DjND5drZJH%2BTfPdemR%2FbsdYL73eP1QOj2Sy5M9VGyrAP2SPWSB7prVdS1F5PUQNEfn%2FL%2BT5NlhGiu%2Fm33rS5wqYnTqZ&X-Amz-Signature=a2c5fd2e011402f89bedccd1f3e31cd6c231ecf805553c6c26ffd32f3b17e97a&X-Amz-SignedHeaders=host&x-id=GetObject)
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