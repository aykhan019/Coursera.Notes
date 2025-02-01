

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=03dd3436d239c14639849b8d66def6bd77a452fa8009133b46c55cf6c7984be1&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=0e365c21d0adde42f26fa54fa424f47c6741a202594027787af807a8a1bf48c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=6a1a462c2fe04f20f0a3ee94866a68d48e56f96c3004ce68b413cb07e9ffc2f4&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=37f508611241f6952a8dda3dd0c9db84a87011b84733012abc2289fee5142c78&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=102eb875c56d4d8ad4fb2e40085dd278b87b3d186b4d8d075f538617bea1d0f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=6dd6413515a2f17a99bfe76b9888f7d4e9617545c9a938608df1f3b3d3ee050e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=02f14ab60819bda42c26b5255f7294a8cd71bb6a5e5af915241b2885e284a83b&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=bb03d193133449eb8af3526fd8c06bfb8a7925391b782b0fe2f7ae18c481fa4e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=85f398b8940497054d2b70a8a2df0277cfce7531dca50f6fd4e111df7169decb&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FZ6D5W5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB057vnYhXs1GlUbEcz5aNSNW6AtRRGMZfyuS9d74gMuAiEA8FpzXfrmSmvDWuwxqUl%2FQSAhR4ede2FiUm%2FrRQCxcoEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPrcqBf6JNygxakxCrcA4bey3ewp7XZ42XhntxhY4C6eoGmUIGzMvyrbt2DegYGJcaqt1xQGXAvsnkqFHPijAVLnl%2BhD8SgEPuDHxervpydf%2B0gvWSn3XP0fKdg7jRrLlaOos6mDCE%2FPG1gkj1jWERn7tH%2FEfFro867dCk71Lsk4HddPOdsqBFBBn4Z%2BtzIBO1wXDGhwJZ7s9QstSRPU48K9PbhUxnG%2FG0KLZXIyXKE4bCNZxLEA391MjLy9IEqnlHwrTVktkYRPKX%2FnZu2ykl5gRzEnREQcywsRwg109A9BTPwyHAFR4fI51E%2BNCCLiTMukAxm7DV4CkHzVqKp7whnJH5gUjYOlwIPSTQWuoOlTqQeDWm8v6xyMNAtrAwe0s9Paz7GHlslHktBvOyZx3YoE%2FT%2FTjpnHUKzhws7m9w%2FcFS89EbyhoZf5GyyFxkUWFhtuUV0bW6mtYjCn%2BQmWGbz6rOMYoRs7juMV%2BgWg6pu%2Fb1q7Fsgq0GfHKWHo4G8BpIhCS0oBR4Af5sdRMP%2Fto46YyngkaZAfpyOjCLiaqEDdIrsCCtlwS2kqF8bMzuEe0Bw5cvJKJdbOME1qSM2TCkHagsx5byfW0yIdhF5oxbOAoajAAdTXeDTlm9Itd8QQX1J8D7Azm0UeoI4MOek97wGOqUB4ciwWhV0f8%2F6BMU6uNBShxsGXBQgC6EQBxaeQ9GKbIR6S34iJJX10LaSmFdVqaBQ2%2Br0G8pgBuChSPOgk2BfyVnc6%2Bqf4%2B9GB2FKMrNI0aUn%2FPrJuf5HMD4IE4riGqS%2Fr8XuSBFFsNzfqvjHBntqyTJG9qLxTwkTH9sc51CD%2F7gCY4rN4rCjEIStvIkLfqwYjybCFDJbOx7s5LQsoQrRge%2BZiNMu&X-Amz-Signature=9cd1d035d7d77f307a04f62055757d97434509903d08f79af793c24c8a2ca501&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FZ6D5W5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB057vnYhXs1GlUbEcz5aNSNW6AtRRGMZfyuS9d74gMuAiEA8FpzXfrmSmvDWuwxqUl%2FQSAhR4ede2FiUm%2FrRQCxcoEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPrcqBf6JNygxakxCrcA4bey3ewp7XZ42XhntxhY4C6eoGmUIGzMvyrbt2DegYGJcaqt1xQGXAvsnkqFHPijAVLnl%2BhD8SgEPuDHxervpydf%2B0gvWSn3XP0fKdg7jRrLlaOos6mDCE%2FPG1gkj1jWERn7tH%2FEfFro867dCk71Lsk4HddPOdsqBFBBn4Z%2BtzIBO1wXDGhwJZ7s9QstSRPU48K9PbhUxnG%2FG0KLZXIyXKE4bCNZxLEA391MjLy9IEqnlHwrTVktkYRPKX%2FnZu2ykl5gRzEnREQcywsRwg109A9BTPwyHAFR4fI51E%2BNCCLiTMukAxm7DV4CkHzVqKp7whnJH5gUjYOlwIPSTQWuoOlTqQeDWm8v6xyMNAtrAwe0s9Paz7GHlslHktBvOyZx3YoE%2FT%2FTjpnHUKzhws7m9w%2FcFS89EbyhoZf5GyyFxkUWFhtuUV0bW6mtYjCn%2BQmWGbz6rOMYoRs7juMV%2BgWg6pu%2Fb1q7Fsgq0GfHKWHo4G8BpIhCS0oBR4Af5sdRMP%2Fto46YyngkaZAfpyOjCLiaqEDdIrsCCtlwS2kqF8bMzuEe0Bw5cvJKJdbOME1qSM2TCkHagsx5byfW0yIdhF5oxbOAoajAAdTXeDTlm9Itd8QQX1J8D7Azm0UeoI4MOek97wGOqUB4ciwWhV0f8%2F6BMU6uNBShxsGXBQgC6EQBxaeQ9GKbIR6S34iJJX10LaSmFdVqaBQ2%2Br0G8pgBuChSPOgk2BfyVnc6%2Bqf4%2B9GB2FKMrNI0aUn%2FPrJuf5HMD4IE4riGqS%2Fr8XuSBFFsNzfqvjHBntqyTJG9qLxTwkTH9sc51CD%2F7gCY4rN4rCjEIStvIkLfqwYjybCFDJbOx7s5LQsoQrRge%2BZiNMu&X-Amz-Signature=130ded5e4d2a21d679d52c2c9f8673ccf8efdff75b1e678325b57cc681504703&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FZ6D5W5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB057vnYhXs1GlUbEcz5aNSNW6AtRRGMZfyuS9d74gMuAiEA8FpzXfrmSmvDWuwxqUl%2FQSAhR4ede2FiUm%2FrRQCxcoEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPPrcqBf6JNygxakxCrcA4bey3ewp7XZ42XhntxhY4C6eoGmUIGzMvyrbt2DegYGJcaqt1xQGXAvsnkqFHPijAVLnl%2BhD8SgEPuDHxervpydf%2B0gvWSn3XP0fKdg7jRrLlaOos6mDCE%2FPG1gkj1jWERn7tH%2FEfFro867dCk71Lsk4HddPOdsqBFBBn4Z%2BtzIBO1wXDGhwJZ7s9QstSRPU48K9PbhUxnG%2FG0KLZXIyXKE4bCNZxLEA391MjLy9IEqnlHwrTVktkYRPKX%2FnZu2ykl5gRzEnREQcywsRwg109A9BTPwyHAFR4fI51E%2BNCCLiTMukAxm7DV4CkHzVqKp7whnJH5gUjYOlwIPSTQWuoOlTqQeDWm8v6xyMNAtrAwe0s9Paz7GHlslHktBvOyZx3YoE%2FT%2FTjpnHUKzhws7m9w%2FcFS89EbyhoZf5GyyFxkUWFhtuUV0bW6mtYjCn%2BQmWGbz6rOMYoRs7juMV%2BgWg6pu%2Fb1q7Fsgq0GfHKWHo4G8BpIhCS0oBR4Af5sdRMP%2Fto46YyngkaZAfpyOjCLiaqEDdIrsCCtlwS2kqF8bMzuEe0Bw5cvJKJdbOME1qSM2TCkHagsx5byfW0yIdhF5oxbOAoajAAdTXeDTlm9Itd8QQX1J8D7Azm0UeoI4MOek97wGOqUB4ciwWhV0f8%2F6BMU6uNBShxsGXBQgC6EQBxaeQ9GKbIR6S34iJJX10LaSmFdVqaBQ2%2Br0G8pgBuChSPOgk2BfyVnc6%2Bqf4%2B9GB2FKMrNI0aUn%2FPrJuf5HMD4IE4riGqS%2Fr8XuSBFFsNzfqvjHBntqyTJG9qLxTwkTH9sc51CD%2F7gCY4rN4rCjEIStvIkLfqwYjybCFDJbOx7s5LQsoQrRge%2BZiNMu&X-Amz-Signature=0be646dad761603c53d43b26a43e33265644477ca2521bf308db5cd1e2951753&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=016912b1ab18656a361263362de382bc52cdf7ea07e809353521f6f8d05e3d49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=4cf002146e1efbec1e9b36776da226769eda8333db66a67d10e5da4e8d83c544&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=de7b7670013c2e1a1daef47c59d38c3c7a6b7f4bf36452acaebb34748f1a3ee8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=5668b2d7a8b7963f52f1d3a322bcb8ce2d41532de60700cb908e959600cd1230&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=1d4e1913ae88c8001bc10bdb307ec54fcfd6e95abab39eecf1005c25fe0062c2&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYOAH7TA%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDb2kqQAwH9%2BN4Wu%2ByJrFaoZq7P3gO0UM%2FmIVca%2F6qKNAiBbAXLSP40%2BWRrN9AC26wdofKYzNUnP%2F3WfeOZZqRTNoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlHObXEofHeONY89YKtwDmGIdtWxp6hAD9WmtuI%2BGmIaZ9AXA1dSEqeSnY7fu%2BamumP9N8I1ynZ9Jo4Hf0%2FZMQdEOblp3XK4R47iqZV68WXSRhKkv6DwTMV6e6OMO7xBrIYlCLWbZncCVi1cdvHmJr%2FegVMsBlxMvcDJOBGPsATM1ShtKcCCDrpOVOnORL%2FAeRWQfPfyEKUI1hwKjgBccmUmZEr9uf2mMUlerA4Lz8W%2BGxnl62iZhMWKKQz7pT%2B6i1kjLrqZSskkleBQn2IIWWKtG0fvuwq5HBhQtlfbEOTqvxcTh7AfuBbEjTina%2FuR5Y1MRoCbgwIP2kV%2BQubXaGWAMlmK7yerbIQMaUcrgrST2ixQVRch%2FsIfzT0%2BTgGd4HsktB%2FLFcglGHHm7L2ThjdCKCLpoaBN5uOvB4GgZ7hGBxPBZq1VkyuZ%2FctpLGDv2kgQ487wD5U5aHsdIPRKeM4b99sk7LisT56320LypCC0GJq3w%2BZgfd34dbs%2BY7zN1F2dxMcN1GRSZhLV2vuf3ycrQ9vLGfswiaW9cQ7nCLFoxTXSGqIFqHcQwRbXOcEASP%2F4Fd4MiBgqSuYvrr1VdYHnWKpvw5N9KD53oqEe6vAj6dBMqbZrCvHfWpkSq5Bl1gyFhkurz9p0bZjkw0aT3vAY6pgFBOVxlAcR3L1%2BWMPL9OD9uHpNFwDxLzExADyHSP4Jd37YbVaiiOQuCgzae%2BiGpo8VfEGsTdI%2BwZe6s1OqwxaDcc4UKpxf7%2F0JgW3duFF1D6KgKXSZRpK3RYK%2FgpIUl5j15Qh8iLiXMk3saY3%2ByV0G8znxO2MpnW8JBb68dwQ71bAgyPf0d968OLTh4FHGSfuehhG7OchAZXQtCn7r%2BD4pWRrsQ%2BL1g&X-Amz-Signature=c5e00f3d40ff9d0db630620132764d67581f2cbfe1f81325de4fbebda50b5950&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ7E5PD6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDUm5NZBDbVzufBPNfKnwBsxGZuqexe0VCf8AGAPd0MKAiApTzrqplPn4Cyu0EHXZ06Ukb%2FPfmlV8w5c8nuNhK97mSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFmHUMEPaQVE9LFAxKtwDTYCSJPAk42mHFTSpa2iVOz1Mvl22mLPZB2ZYW1Fbk1%2Fp1XB%2F3jZlbhNTvEzw4N81c5cXTPBItHoux7CWKxe5MkE8JCWeVskns5aaIWvPzjKXPK0CmzhkFpX%2FZVKekLhPpGfjWfkkvRAgBVeaKL8ZzfZ2HeAARdpC6RMIVlrqanPAz%2BfqWkbVfm75VUR5FPy%2B%2BzyYkmGNgQg%2Bb6V5dctmlQ3CWK4yX78QI9L7fGP4mUZ1fqX7JuWijIGxgL3cuNsVqJh%2FC%2FIW3Xj9PNwW0kRYSV%2BJcQXT%2BwoBvvYLsRnQJl%2FUAi7e5%2BUpbzCWTaedZaHwCdJu1GsGVOdv0behp0T%2BrpRhAzErN6jlSg5MkapMWfWADCPYYqAQNu7qEdkhXiAz0AMr%2BusoMQvwlrt24to1E4f5YFuYJc5Ui%2BO73r4%2BaQSLdaIZBaVUZ1Bjp0g9hqbLVLsnUR0JXba31RCJi4NvwMWNjMyYIVbsM5UBTnXf2La760Myuwjl%2BOgu4S720HYPk2FU4uXiDTnseP9ZguEVsxsrOZfDdd4%2FNiJRuW2%2BVkzj%2F8fd0PWDiC%2Fs7c0JAPi4Av6Aee%2F1U4QlUn7j6ByRDkO9vwrjGUlMLbWoTzONhfbdlfQ23IGbvA44cEIwvqT3vAY6pgHZhIroZw7XTEdNbMs6leXMJx3nAnsHlPdjVn4LNOwAIKauUmaOes5h18Ihsp5zngBplbWOuB%2BWgVsxYCC4h7kskZO2hInrfDMc%2Bdlc7Wf6H5RFfl4AY3kvaaT1jO2q9SrtCm2dMs6k%2BsW6VwLac15JWx9ER4gyMijQv38vKT3IshxS9dVQlwzgtouDDFbXkBo59OUYLZnDVNw1e3RRcCoELL1WbspO&X-Amz-Signature=7352cc611b33a60113a56aa758b40fff7628fc69ade23e549ee7b939d953247e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ7E5PD6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDUm5NZBDbVzufBPNfKnwBsxGZuqexe0VCf8AGAPd0MKAiApTzrqplPn4Cyu0EHXZ06Ukb%2FPfmlV8w5c8nuNhK97mSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFmHUMEPaQVE9LFAxKtwDTYCSJPAk42mHFTSpa2iVOz1Mvl22mLPZB2ZYW1Fbk1%2Fp1XB%2F3jZlbhNTvEzw4N81c5cXTPBItHoux7CWKxe5MkE8JCWeVskns5aaIWvPzjKXPK0CmzhkFpX%2FZVKekLhPpGfjWfkkvRAgBVeaKL8ZzfZ2HeAARdpC6RMIVlrqanPAz%2BfqWkbVfm75VUR5FPy%2B%2BzyYkmGNgQg%2Bb6V5dctmlQ3CWK4yX78QI9L7fGP4mUZ1fqX7JuWijIGxgL3cuNsVqJh%2FC%2FIW3Xj9PNwW0kRYSV%2BJcQXT%2BwoBvvYLsRnQJl%2FUAi7e5%2BUpbzCWTaedZaHwCdJu1GsGVOdv0behp0T%2BrpRhAzErN6jlSg5MkapMWfWADCPYYqAQNu7qEdkhXiAz0AMr%2BusoMQvwlrt24to1E4f5YFuYJc5Ui%2BO73r4%2BaQSLdaIZBaVUZ1Bjp0g9hqbLVLsnUR0JXba31RCJi4NvwMWNjMyYIVbsM5UBTnXf2La760Myuwjl%2BOgu4S720HYPk2FU4uXiDTnseP9ZguEVsxsrOZfDdd4%2FNiJRuW2%2BVkzj%2F8fd0PWDiC%2Fs7c0JAPi4Av6Aee%2F1U4QlUn7j6ByRDkO9vwrjGUlMLbWoTzONhfbdlfQ23IGbvA44cEIwvqT3vAY6pgHZhIroZw7XTEdNbMs6leXMJx3nAnsHlPdjVn4LNOwAIKauUmaOes5h18Ihsp5zngBplbWOuB%2BWgVsxYCC4h7kskZO2hInrfDMc%2Bdlc7Wf6H5RFfl4AY3kvaaT1jO2q9SrtCm2dMs6k%2BsW6VwLac15JWx9ER4gyMijQv38vKT3IshxS9dVQlwzgtouDDFbXkBo59OUYLZnDVNw1e3RRcCoELL1WbspO&X-Amz-Signature=d20bc7adfe6fb1116d7b1e938e39c95cedea689b7772752408bf35acea88d6e4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMZ37ICC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH4Y7t8FRI55MnUQSx5Wd6P6q2vfkcF4ELiD1LXp2YmuAiEAn0vadC34m7GQE2ybYye4WGA%2F2mtZpmGi5U7iEPvu3lAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPOz8x%2BlVO3bjXKRircA8nirnzvcS%2FxO1bW2AZzEPmfHZu0lwf3aXt5dGoRfz8cAYS1ZVJ8rBZlPh4ycJ4CUJ3UTZUf96ID8hxpGc5lnU%2FoDxro67kGxrl0L%2FWH%2F1jojnm0zi7AjlEHT9augJ9ewUW6ZyCl7YEhtD3VFhdHtdn03y%2BnfscLuUNKB%2B58KA61B%2FMrjxALf3iGOPTEwNGMXyJPZSP4JVfknyoCtcXEsa3SJpxYfEzXP0DzCTyVZWL7LlnbAD%2B6Fs33NbPRjmr814pyqV0x8cQFQ0Mk9OdNaAI2NVDMgzH%2FVZehxwAbgDD87gpyJivX4cX%2BT5hyUQYZJEuRQMz3Hss3o3N0LoijFSJL7g7QWu7gLz0D2wdgL%2FuCsvFCJOdDfG5Qqv6AP6z4TPzvsRExdvQsVvphOBSrsbEgtjtNwE6tMJMCD1gwlr72uc0Nyft9BBnK6TQzMV3osZBWi9XjxWU%2B%2BBb0nwqlow6DPArvnzi0co4mPS9bhGdxbMVa2OISEMo7M4TnqtM9PQWRlCj7TYQcsL%2FsFlFHAqgB%2FvIi%2Bd8G24Uosysf6BMGH4QRncWdaJGFGpaXAaYd%2BgEE9z8HoY4sgFcR9692Eg2QJEUyWSe9QhHvK9LZw4bn2WsEzUbqfHj9%2BPSDMN2k97wGOqUBmJ9Vtih4RygPN%2FgAbpTFUfYDH0f3%2FnxUegeoi1piJvh6KahLbz73d2%2BztfHusVS8LNX0B9Zc%2Bn1wiHO9ZE2dvxjmnAmkwzfuDuVHajrcArTG13yOGuo8JR5V0OBQ%2BUmYqWrRdEl0IVA4ssl473B5g%2FAv2z48%2FOGFBcqHAQKX9cXlblk952lXGJl%2FKUCb2It52JlfVM2JzOdnWNEWm4xOeI%2BMmI1n&X-Amz-Signature=28844644615da4d1fb59686399d2134477bec3514b37b6a2abcc051f47b3cbd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQIWJVFF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T131524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHL6Gx7YfZtBDt8ic4%2FJov0iXRGNwv8%2FXsQOShTG17qyAiEApPUWnGnH5gA2ng51tOBvkh%2F%2BgxZv0D5pUbhG%2Bh0T3OAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBJi5LjaehAPKOZ%2BCrcAwP6zwEVJUazvKEUhEbLE0MBveVK0VfW6nOAH0WEPuniM0DQazLdh1Tw3HiejMFjMeDBVpq1768ycD9ZSKSC6O4nNAC2%2FYGH8UipkSaJUYlBotoffpRDPb2nrGHAWsNAukzhZ1PYvrd1cYk0dLBTfsyETIkVL7lGJbz2Bm%2BXS0Id5JbBU2nbXvOy%2Bj4gqn429MG14Q2XUH01tpQYv91wAqEk6z2nsGkgI1UPsIKOogtJftJH%2FUL5pewwsRvE57HFS9Q1qkegqIJWlotI%2FsTnlLvHqwzofI9FJfAulEd4P4QSV2xaRTVGT4DoyozIn5f3rNnzoGABGxS6MC%2FzuJhSp8fX2ZMDUZNG7g5QhA6itUFRim0TFYHeUxHoER8l9oo2MW4ey1bK%2FDee%2BWz4Za7fvNAEoZU7NDhzI2ez1RcRHWsmCb%2BXaeiGlSf3rrVVR9zCnRlHihtkKMowJkYTM7GWJhcLzr5GTMKvo9gijd%2BXwkbD%2FMhJkgHWtLnIiGeFimghL6JTsCxfORukY3P7GynPiRtlgg72j8mn7lgC7b%2BiZDiHjv89usJbK7goMWONiX3VL9J0LFu4bscfFCG4YIBrgl1bHNo0WUVNJFE41U54VYJ6fJXWQTbZ7d8bXrwuMN2k97wGOqUB79%2B%2Bz6jpvzn6ae63ANDVCxYMJDRGBMyDrELNr5EFgoq6tBY0dtxJekLhUmRZwgkSERiOt964yMx4HopWK2NfDH9G8kqquXnba4aZQSYeLOZG15fagnMUweFic5P5WIG0rLezrdARc5h4VKisMBExh9KkJwAlCfaKITz0npADECnWQbvODAp4r7v%2BPW4RXt%2FJLnERHyWuxRd6YBlAuVlwiipAxTvB&X-Amz-Signature=7b5243eda5e9090713b9331b2a67833da0c930913df34f8a13645452dd749bb6&X-Amz-SignedHeaders=host&x-id=GetObject)
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