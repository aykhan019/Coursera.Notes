

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=4b86f6563d02c455c21a2ad8f1304ea44ba06a4c376c3c9b2141eebc18ba563f&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=10b5e66016409dad2ea541f8f099bd9aaa3085943c8cf070c5156373cc07b295&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=7c2425caec54f876f5024836a92223f224cb851c8c1f059ac15dd2bc96a17aba&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=3aa8433eaa0d5d32cbd65e49a266dd50928d3445d9da52eec77096d0c813aa16&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=ef01a9f75ba4995705b7dd90c370afabdd046f6338095573842da4d8826e4f18&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=d9e15a7d2f718e8b92e2b23606e3943d9c22b459305f6d2c02b668237aefbe56&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=22f9cc8ab8dfc3375dde7bc3f71d98727a180ff50089724830abf2d9e4a22ac7&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=ee818118187fd98bd8c84463e28753ef1487f78a2a37f2a4d5695785bc3f8021&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=e9ae5eff8d5ee5e99d1b1671f4862d9c3febd3668b7f2c07e76ba298975cf38c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2P6JHAE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQD2okoRUuTZjPyupsGUT7Cycbtub3lCthUH%2B2kuaHGkcgIgD2iPnsm7uOUxe%2F6RjErLHW4cd%2BmxRPtkiRW8lishZiwqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIdWlVxz%2FAdAP%2BVBjyrcA%2Biw31gQUJD8rMInyp2yjwsdffbQO5frD72%2BNAQp9r8PSzKIXzBKhtPV9WW4ouJ7OcOFJkYqn1Zp44Md4MIR%2FmkRvz7GOICCAYSh%2FEytF0vppol0v6erooK%2FrNYgiXrL3aZruvgwwj15DYDcp7JVQuqzKs8r1cm%2BAdq2ewicknYdyrtjTld8JBLksHi3PLv5sgke72QNg93Te6fjpVgaLzRCS39LLkQE8HpY922eYQvmBrPLLWtYiGNNbn%2FO%2BciUS8cM1isCvYnqsMi7xRfG6X9r5P8ylcJO69h37xNz6kN9vGYGtKKmcrzGUT3JGcb%2BRmPHTaG7mk4vI5vtWskKH8t0KKxSuiIIknd8gwvWTYFV9oTOv61wIXd46dSrNd1cBc0H31eyj4ewlsYifEEnxBH4n3r7AV6kupYAda%2BMLh1GfpUwSF9E%2F1hDgyahFkv9eWnu7czvgkniBPwefwauGI57VBwOUWn4fDZDcQ%2FWen7Q0pA%2BAAJJWKa2Vn8mRlgUXGEcE6CQZY%2FkR02KJT8nAEVyx2ckvdQNVI7FuUObVXiGONvt8ULclrRqwkaP1zBO0LgWu6eU6jPmJaScGh%2FNKPcC1emYgPfuqsfCZnO0SFmQB0dK8WNzMxmS10cLMMGFnb0GOqUBQ7k7YAZQOD0geWusb%2Fd8X8HeFVk3QvAGnO8TiQa01wsdXYw1FuceXh2iw97lp18FAQZMfAESsZb4RPL30AEy0goGTg70%2FxBUyps36KglI8Gs%2BtvxMaUdajPXlaHozsWJmkyjZkebfDv2112o%2FvmvePhgdtZZMLNALPDnsM25Ht8Cv1AEpLLPQZlssu%2FYwCiVL80q1Cjf78BeGimjwGw%2BzZtSFMyj&X-Amz-Signature=bbfa0146314185c2ee34a6c5099cc461716fb6230ab445a8c47382467bc8fac1&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2P6JHAE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQD2okoRUuTZjPyupsGUT7Cycbtub3lCthUH%2B2kuaHGkcgIgD2iPnsm7uOUxe%2F6RjErLHW4cd%2BmxRPtkiRW8lishZiwqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIdWlVxz%2FAdAP%2BVBjyrcA%2Biw31gQUJD8rMInyp2yjwsdffbQO5frD72%2BNAQp9r8PSzKIXzBKhtPV9WW4ouJ7OcOFJkYqn1Zp44Md4MIR%2FmkRvz7GOICCAYSh%2FEytF0vppol0v6erooK%2FrNYgiXrL3aZruvgwwj15DYDcp7JVQuqzKs8r1cm%2BAdq2ewicknYdyrtjTld8JBLksHi3PLv5sgke72QNg93Te6fjpVgaLzRCS39LLkQE8HpY922eYQvmBrPLLWtYiGNNbn%2FO%2BciUS8cM1isCvYnqsMi7xRfG6X9r5P8ylcJO69h37xNz6kN9vGYGtKKmcrzGUT3JGcb%2BRmPHTaG7mk4vI5vtWskKH8t0KKxSuiIIknd8gwvWTYFV9oTOv61wIXd46dSrNd1cBc0H31eyj4ewlsYifEEnxBH4n3r7AV6kupYAda%2BMLh1GfpUwSF9E%2F1hDgyahFkv9eWnu7czvgkniBPwefwauGI57VBwOUWn4fDZDcQ%2FWen7Q0pA%2BAAJJWKa2Vn8mRlgUXGEcE6CQZY%2FkR02KJT8nAEVyx2ckvdQNVI7FuUObVXiGONvt8ULclrRqwkaP1zBO0LgWu6eU6jPmJaScGh%2FNKPcC1emYgPfuqsfCZnO0SFmQB0dK8WNzMxmS10cLMMGFnb0GOqUBQ7k7YAZQOD0geWusb%2Fd8X8HeFVk3QvAGnO8TiQa01wsdXYw1FuceXh2iw97lp18FAQZMfAESsZb4RPL30AEy0goGTg70%2FxBUyps36KglI8Gs%2BtvxMaUdajPXlaHozsWJmkyjZkebfDv2112o%2FvmvePhgdtZZMLNALPDnsM25Ht8Cv1AEpLLPQZlssu%2FYwCiVL80q1Cjf78BeGimjwGw%2BzZtSFMyj&X-Amz-Signature=64dca48550b7d4ce8e27e805d5801399b4eb8f54689fdd0a23d2126d4f423bcd&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2P6JHAE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQD2okoRUuTZjPyupsGUT7Cycbtub3lCthUH%2B2kuaHGkcgIgD2iPnsm7uOUxe%2F6RjErLHW4cd%2BmxRPtkiRW8lishZiwqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIdWlVxz%2FAdAP%2BVBjyrcA%2Biw31gQUJD8rMInyp2yjwsdffbQO5frD72%2BNAQp9r8PSzKIXzBKhtPV9WW4ouJ7OcOFJkYqn1Zp44Md4MIR%2FmkRvz7GOICCAYSh%2FEytF0vppol0v6erooK%2FrNYgiXrL3aZruvgwwj15DYDcp7JVQuqzKs8r1cm%2BAdq2ewicknYdyrtjTld8JBLksHi3PLv5sgke72QNg93Te6fjpVgaLzRCS39LLkQE8HpY922eYQvmBrPLLWtYiGNNbn%2FO%2BciUS8cM1isCvYnqsMi7xRfG6X9r5P8ylcJO69h37xNz6kN9vGYGtKKmcrzGUT3JGcb%2BRmPHTaG7mk4vI5vtWskKH8t0KKxSuiIIknd8gwvWTYFV9oTOv61wIXd46dSrNd1cBc0H31eyj4ewlsYifEEnxBH4n3r7AV6kupYAda%2BMLh1GfpUwSF9E%2F1hDgyahFkv9eWnu7czvgkniBPwefwauGI57VBwOUWn4fDZDcQ%2FWen7Q0pA%2BAAJJWKa2Vn8mRlgUXGEcE6CQZY%2FkR02KJT8nAEVyx2ckvdQNVI7FuUObVXiGONvt8ULclrRqwkaP1zBO0LgWu6eU6jPmJaScGh%2FNKPcC1emYgPfuqsfCZnO0SFmQB0dK8WNzMxmS10cLMMGFnb0GOqUBQ7k7YAZQOD0geWusb%2Fd8X8HeFVk3QvAGnO8TiQa01wsdXYw1FuceXh2iw97lp18FAQZMfAESsZb4RPL30AEy0goGTg70%2FxBUyps36KglI8Gs%2BtvxMaUdajPXlaHozsWJmkyjZkebfDv2112o%2FvmvePhgdtZZMLNALPDnsM25Ht8Cv1AEpLLPQZlssu%2FYwCiVL80q1Cjf78BeGimjwGw%2BzZtSFMyj&X-Amz-Signature=b9041414d1ff7769f3e5904ac178088d7fe2090f3a70e818b30a8c1f58934faa&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=19be700881b1f703d9fd21f5945b8d632bf3949a8f686597b6cec5af2df7f637&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=6d75e2617394f77a92afe6860dcd738368e9090152c8613a094e1a6111078e81&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=cc5bdfde384cc0164c5d6703f8651e5091bc0035c962a6e766d8f6baf41b0075&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=5d7883dff4bc158f2f9983610bf44c533af84776bc854c6eb842c50cb5d0166a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=3d35b8eaf92364e4b53d58d445c30b1890a55e6627393a84c78ddec0cdee7e37&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZEI4ME6%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCtajFl2FltbiL7%2FOtUNwl77vLLmrb7iY1akkTtxqNl%2FgIhAIjNZn3KxGO5IijcOauTeNhTD8IPvNpT5vbCsxDBa%2FejKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTSieLWmwuEFhC6SMq3ANswWTXHhD82vCVxKxKU%2FCvNGmjEdD9A%2F%2Fy8BAu0cKuLuTn2DTdNAJank4XnsftqcbR6lcYA2rPYobxXh%2BJIZFe1Uta162f5E4N4%2B6rn%2FjgDmZ3M2FGZqUWUVe5znIyUUA3KCVL6ifNMkuwHDkubrtfDqCSbv72x2UEA7T%2FTAGC%2Ftz7L1LpxZdw2YiwBxteMkN1eyDaY%2BK9F8wZQZh34vaNQjObgYSSOz4Ei1KODlR0gW%2FNkyAfylbxj9AetoWbFkDNJgDOKoHpJ%2FDjg1GYmhENFcnBfdYy8lzziE80bZr%2BYA2KLciSbPqIlBYEbEHkDi%2BfNi379jC2gbLsmshzvGeQv2FqU%2BHDjDx2FQ2F5Qralm8h9QqU5T4qOTI999N7qSYmC8ueht%2FY%2BsGYR2kO68eXqkb54PQHWLtLZeDfxxLI7JwoZyjD7MIHWgC1OKUOFLXvjB9XHk1YJMp8pJZEo3aVlJEazDDhweYa3KJwCTlQ7gUNrzsUaA1YHE58%2FfU%2FsBidKOHwZHIzVKQjstHtjl0YuSpRJYY6sdopOYpR3pRgek923SvtjxWNB6lzlQT6bOw8u5f2f93kJg3iQu3HES%2ByefWv1m%2FVKzRV%2FOQeD1DcJhuljk0oP7exZ1k0mTC8hZ29BjqkAcus5NG7nP5CeKZ%2FqFvYtPCF3qRg62mGg9zp%2F61S8aAXhB%2Fj6BoDt4WtejhBe7D%2F1cJFj%2Fmk3XSX9MWoQ%2Fjvt0m1r2QJcwlTQ4sRYzov6BpCCrIRNR6zdM92PeNYC%2BbrE5IW3628qwgHduvHOIiLmgd4SGmy%2FZbxPcyszdBkYBvqDF5TLjPZn9rMnrIsksEE%2FrMxOSVAi%2BbBRVPQuXORh1ljSLX2&X-Amz-Signature=b6c520bed89abbc6153efae2c1da2ba52569f5fd7b6e096a2f2d06dff0fb11ff&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2XWUU7N%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGIjGifUttzdn6h1N4UNwWtcOuYMcLMZp0zdZrwr3EM7AiAFBA1jp%2FBEKbBqeMH4z8TJmx%2F060xzNIAFq43zogXggCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQnke5E36cLQ11xGlKtwDusETcpCklHw38oWmMN7gW1oFY4GVyFiuK7PdH2KNl6%2Bn%2Bp1irG9GLLS5asSfnOomcD6b4F5MBmHiQLCyWOGEgfbV3IowGDdSM3kJ53q8XRuaiUzH%2FUBehGJRyJz5AilVKY0DqdCjd%2FrtE3UUVlGo6TFUjPUyFaZ%2BOLmGNHrLzxzzlRhzMmXprDOeG3fZOabewEVZuLyrJEP4VJydGWY%2Bi%2B9q9%2BMA36IxhZ3DPAsjPpg%2ByAZ6gPnDOxhOUlLU2G325pekvWP%2Fsanwyx66T2nvUZ%2FfuAVNG%2FhFhtXb4icjvHCsWrkiQijvNUv372bS%2BLLyAReiDrwWP0oixCvlBbvV18nBsAUmHxJECfdOvpJW4J7W%2BhC%2BW6nJ7uoqLK1tiF4J6Y2fJyrlU8IIrUoCMHWCJBCZ%2BGS%2FcDJwvzGHmQrPGSe3iluYOx0kDQi6UlZI83V82c1EIMS5Qzn86slkAF%2FkzpVaQFV0tHhchb%2BU8NrtGvqLVfyxwn%2Fm9vT4Nh8DwuvtRaIKAuyzOiH3wsuEs49ltY9BpfjKqVu%2FpYBcuoxbVkq1pq%2BPXA8FMzcGR9ZEorYwfSgfX4sT2tH6wjVcNOGwjw3KCx6yVEh7tDPAd4pLx5UZ97zS9%2F22q%2BEfq%2B4wgYWdvQY6pgEiTs2fz0MwB%2BJAo6GZHufoCrrdAYkUfORg0Sztr6MYt50ddDf1Cluvd3UHa%2FqTLAxOoOZJEOn9CJGGF6XCqRFGhsRWt%2F4RI%2BNLzrZxuDZLnlX%2Fb5zQpAfhcF1A3VVTmwcIGMqsBES696njtAlBGiG8505jf%2Bh%2FEehyssu4a1e6OPSPqsDiHXi0G6bVQh7qtTWR2TUgOysY4ioSrjqCxG%2BqTyg9iA7q&X-Amz-Signature=c8eeb6828af5126d1f1d82749b0a9c150a456d7bd0a9fb4de74b0ed46adc7472&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2XWUU7N%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGIjGifUttzdn6h1N4UNwWtcOuYMcLMZp0zdZrwr3EM7AiAFBA1jp%2FBEKbBqeMH4z8TJmx%2F060xzNIAFq43zogXggCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQnke5E36cLQ11xGlKtwDusETcpCklHw38oWmMN7gW1oFY4GVyFiuK7PdH2KNl6%2Bn%2Bp1irG9GLLS5asSfnOomcD6b4F5MBmHiQLCyWOGEgfbV3IowGDdSM3kJ53q8XRuaiUzH%2FUBehGJRyJz5AilVKY0DqdCjd%2FrtE3UUVlGo6TFUjPUyFaZ%2BOLmGNHrLzxzzlRhzMmXprDOeG3fZOabewEVZuLyrJEP4VJydGWY%2Bi%2B9q9%2BMA36IxhZ3DPAsjPpg%2ByAZ6gPnDOxhOUlLU2G325pekvWP%2Fsanwyx66T2nvUZ%2FfuAVNG%2FhFhtXb4icjvHCsWrkiQijvNUv372bS%2BLLyAReiDrwWP0oixCvlBbvV18nBsAUmHxJECfdOvpJW4J7W%2BhC%2BW6nJ7uoqLK1tiF4J6Y2fJyrlU8IIrUoCMHWCJBCZ%2BGS%2FcDJwvzGHmQrPGSe3iluYOx0kDQi6UlZI83V82c1EIMS5Qzn86slkAF%2FkzpVaQFV0tHhchb%2BU8NrtGvqLVfyxwn%2Fm9vT4Nh8DwuvtRaIKAuyzOiH3wsuEs49ltY9BpfjKqVu%2FpYBcuoxbVkq1pq%2BPXA8FMzcGR9ZEorYwfSgfX4sT2tH6wjVcNOGwjw3KCx6yVEh7tDPAd4pLx5UZ97zS9%2F22q%2BEfq%2B4wgYWdvQY6pgEiTs2fz0MwB%2BJAo6GZHufoCrrdAYkUfORg0Sztr6MYt50ddDf1Cluvd3UHa%2FqTLAxOoOZJEOn9CJGGF6XCqRFGhsRWt%2F4RI%2BNLzrZxuDZLnlX%2Fb5zQpAfhcF1A3VVTmwcIGMqsBES696njtAlBGiG8505jf%2Bh%2FEehyssu4a1e6OPSPqsDiHXi0G6bVQh7qtTWR2TUgOysY4ioSrjqCxG%2BqTyg9iA7q&X-Amz-Signature=40181b2b8a908d8f924ac05f1f20e6a1b8b48c219d79d0e8e2d783a42c3861f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBF3ATGC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCx%2FvRlLSq9Tq8x6H5lAjsiYZDQQy0v529vh9JFLYakNgIhAI2m7joKlhusPloHszvXB%2Fx0cIxGEuAV7c5229bj%2FmKnKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqBdyYN4yGUZK%2Bmpoq3AMUU52Iw%2BeMg69xfjqfCawKftMOywlis%2Bl3lE%2Bjr0tBwLR68qUScCYbaV%2FojApNRyiID%2FJBaa9f9V3avgoBgB7aLYrMHGQCbsNeGZvXXE2lYyq9pNPE9gP5yVDJ31RDqzdLORmNM8u8Jj9UlcTJkgUD%2FXgkqvGsC3skMBDNnsSwZt8PqrCL0YfajXcJjk7lGV76%2FyHqY%2BkFfToqa3WknADmvjA2TjO9MxfwsY8QMGIUp%2FL%2Br0bCM6oB2yb2NjtcE0xVViyFlhQEJJWuax4GGxFeTRzsIGxjtx9bY8wGzSsYO%2BI7Jeo15vRb2FC2y1uDVtja741B9CH3k1oPUF02%2FAyp4B5Hfj3XrnnYyaxrqBhy%2FWmqzp50U63o%2FcvqPYdO6y67N4yO4ZJ4L5K55TUAOSaIoVoAl7GHiVP4JRO96tJmiT1OUJm4LgOp2%2Fh1Ba8SMMawDCGCIcGcr9SIRgm0d%2ByKDTpGW6sSxknNhWT7Wf2A7Gx56egRJ9Bf7uGsn%2B2sw%2F%2B7cib5Y9O54yel1BYxVQt%2Fo%2Fyo3sz6cq1ALQHkIE3ciI4rGd9nd38tqYhZXTC36gtjnHzaB4h9iEG6%2FIoQ46MV104Uqnd%2FAYB%2BTb80XcdGbcd2WbaSWbR49N70HTCthZ29BjqkAblxwWUZVCIUdmuV8f%2Btviaj%2BcD8S3O2DfZXvFwuM0zyefhVBJqXTSn9wL5TVM2APbuOkLi1G8mYSbtMcKqdgEETV7hsLtCYCs7VToSdh4BVAS8VHIdozt7jDutjSrzyoQyEakFNq6sM0VjTlZNVRhTiKMJKSx4UdvGOxA7sosbzxKT0akIaOlkrEcm9cir8337dCKUGH%2F0lKAxhKK0wl%2BaZvvJC&X-Amz-Signature=d4f2f04363a489cfdcc5c1c9e693d91c4582c0a1e35b1cb6d1fa54b2f3f5dc41&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NAQKCL2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T131616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQDiTk3uY%2BRy8Bg7oDTVKp6YYV%2F3r3bFiLgOm2nFHsqSVAIgfoP4O5%2FMKaG8%2FopVeFWx8CG0l3C8WITO06sc4o84%2FxEqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKITnXvGAWcrw35RGyrcA2nN76IDxEHjo9FTwHWS1g8A2HQoa6Z7mzCHh0WKG%2BReCzspXuVUiZ5Es8yy6y9qAgjNDrKWVGQcRdoiMkyPfg5de9yY%2FVpZNzBcmuQ4hjgXPJboTPmZxIn9F%2FUUZsKyEkrb0osJxyqAlLSIMLke8CzFmS09D8XrTee5Kj%2FWQOYWKW7QIsq4Kyi%2BgcHO6QRzSmeOQ%2BsWUiYTIzh2uiwWe1XyjM64oDNOOp%2Bx3DEnVSf%2FfyafqSByjupM1Z2bC0wFdFjNznPXhqWTqSxNrRWJWICbnS5whYF%2B9HMBcJARjNXn44rlsOuJaafqXvq0LOiuZUBKn6PmvEal7TIs1GIOlTyQy1tnZPG5CVq%2F4RdS84AykRaBiPzniZhZ30T0UK1K7Ck0AWVstYB03ZjhSSZY160X7ptgNn8RtCqDJcunttXAxYadJRo8udyrTHgLlfh03HrkeYTbDYXsZl%2BBHUoDXXTgI5kqp2WraGTHlJWC46qjIWKaujV5XdTVn%2Bwjh7QAeHvz6tXYNwk2QwvPuHZtuikqp7xg97els6CUFbw3lsGHEu%2BEjYBOitpWN0OXRitmcWHy8ZqAfnBjdQZZ6jHDVVCOZpWZmhO%2FuW6%2B%2FVhI4Ag%2B3%2FAL%2Bo8icbGmMQoLMJKFnb0GOqUBIwwtp1kn9Jk04FnV7%2BjFB2CF%2BlZZ8Dj%2FufMFN0HZRSTzjbDk6rHEANA3PMxGbwefw3UOS%2FGoAr5kEI%2F4Frb0x8%2BRz8R4MJx8wttJpg%2FbeqapHfGF0XGvMeJQNkiutBODjsMWycmeCJiWgEBWlp%2BttaUtmVXwcT3PMk4Ye4fVv%2BTRTg6mkS43Tl%2Fm1tG%2BmQ9pzC6CqviASPQeSm%2BYibKbKjK6mZdt&X-Amz-Signature=ce6f0de3ea50fe3e5652d595f6990da4fb06fc00579a6fae04c4da1ff01482a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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