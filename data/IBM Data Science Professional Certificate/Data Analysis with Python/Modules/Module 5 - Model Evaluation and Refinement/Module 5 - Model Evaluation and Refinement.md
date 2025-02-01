

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=214a2e31573311f569d0e602a42a6b7bd74304e078b2efafac4f07fcb3ab1f1d&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=9f32a9743bd290e65ca408248c741350d10a099528ad019e72a72fcc5fbb577c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=b1c3355d9a262b2016dbfc7d636d5d36f14d765b57ee23dbfa13772ec893cc06&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=19e890cd0b265760aeeecce9dd933a753d2783f3c4efce92ce6fb344239b4bc8&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=12a84f0e1ec7937a3e9f11c1f2ac0f32d11869e8b30a9e11511fe0e3f3f9cf2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=04680279ba6ed3a29941010a2db4a254170a12185e375bf3ce5421baaf15fcf5&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=e3535b9557ce40b2d91a59f9ffef568f3ac0587d4faea660f767d4ddf4590eed&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=e1672eebe1f9e2632c65fd5e3ac5ed4a22f2ea46f537b22576181ada1720c884&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=b26a6297cd10e2c9e968773b2a00e97c6bbb301fcc5d8236e83944d3b8d62e8f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGABESTB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC19SHLLTUxQ4c%2BmIHZ9YiK%2FO4pxl3mTPzdyH69Esi%2BqwIget5mROYTuc%2FAjIAMQ9K8E4218rLmD7%2B32TmwYkG823wqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZv1kiK1swamgnKIyrcAzgr%2BIj9CYgwsyG9TFQB8Nvh9W9VTJyExnt3Xtr01RRdWTDp2gjXXhCNB71fegIsP%2FuT2Q%2BoyyHWAbwSJnpsnoGnOOAwCheItrt%2B%2FrSNAGpzZZfS0bIIiRhXn7X00lG%2BMFKUPihtnQ7I%2B8cV7OUqkSG4YlTCUVjq8xCMAV%2FEvt10cIslQx%2FbgXArILftKfJApHufTwW51OCMCOZEWANbLK8WR%2Fos%2B3LgqQGWS%2F%2BtLCsP9e%2Bgl6UvMKfChlcDzX9zo3OTzO%2FL%2BPj9gA7OqumT3bkEAmHB7BA0EcMRHez4Fy%2BFs2ZcehdVZKU4HHbd70x4zuPp0QhZcKOvLAuzwDA2GmW5X1Rpki82AH2H9HluMDouktd3Z%2BiBxYF0rfsCx%2BSsC5%2BLwwMK8taa48oBP3Ip0Vrbuak5p2A4vd1bJUQYY8t3b%2FGaUqLv6zcnzO5JwiBFOyx%2BsbS3LleT1mdEk4lfemr60OCR1OqUrwG5jrMOaaI8lPUNcqUOJtx7bBqibz3TQ3clHiQIW0bAYhwzpKOcjrAlEYuMuq1T%2BqVARsTKZdl%2BVYfpKA3698tuyw9hbRAmlcVLQvEnlOS2jmglqEaK5k5W%2B71wg2KFDPDI933hP0ScmHO3o2iDxr3OcwXoMLDd9rwGOqUB6TEzA1HUgkoAzT55FI0OXWLwkRVZY1EfuG05Z0qwDxf6zasXTITiGD%2BSHErjKDO9Gy4va8yzZ0vWIChb6lwz8iKx0ovjfW76LFX65aTjwUI%2F8cVfQA8GujbkET0srTI%2BdTB8e%2FrfB1vO1e%2BABvUbO0ltVi1VIvj5I7SDsk%2Fg6gEKnyeICA6GfRMx4vMSS6QIBzcT2Hy3yQWGwQgdBC%2BRHvh%2Bbk%2FE&X-Amz-Signature=71269804913819cbb104b7c058b69145d2702528460cba0255c21315ca5db699&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGABESTB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC19SHLLTUxQ4c%2BmIHZ9YiK%2FO4pxl3mTPzdyH69Esi%2BqwIget5mROYTuc%2FAjIAMQ9K8E4218rLmD7%2B32TmwYkG823wqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZv1kiK1swamgnKIyrcAzgr%2BIj9CYgwsyG9TFQB8Nvh9W9VTJyExnt3Xtr01RRdWTDp2gjXXhCNB71fegIsP%2FuT2Q%2BoyyHWAbwSJnpsnoGnOOAwCheItrt%2B%2FrSNAGpzZZfS0bIIiRhXn7X00lG%2BMFKUPihtnQ7I%2B8cV7OUqkSG4YlTCUVjq8xCMAV%2FEvt10cIslQx%2FbgXArILftKfJApHufTwW51OCMCOZEWANbLK8WR%2Fos%2B3LgqQGWS%2F%2BtLCsP9e%2Bgl6UvMKfChlcDzX9zo3OTzO%2FL%2BPj9gA7OqumT3bkEAmHB7BA0EcMRHez4Fy%2BFs2ZcehdVZKU4HHbd70x4zuPp0QhZcKOvLAuzwDA2GmW5X1Rpki82AH2H9HluMDouktd3Z%2BiBxYF0rfsCx%2BSsC5%2BLwwMK8taa48oBP3Ip0Vrbuak5p2A4vd1bJUQYY8t3b%2FGaUqLv6zcnzO5JwiBFOyx%2BsbS3LleT1mdEk4lfemr60OCR1OqUrwG5jrMOaaI8lPUNcqUOJtx7bBqibz3TQ3clHiQIW0bAYhwzpKOcjrAlEYuMuq1T%2BqVARsTKZdl%2BVYfpKA3698tuyw9hbRAmlcVLQvEnlOS2jmglqEaK5k5W%2B71wg2KFDPDI933hP0ScmHO3o2iDxr3OcwXoMLDd9rwGOqUB6TEzA1HUgkoAzT55FI0OXWLwkRVZY1EfuG05Z0qwDxf6zasXTITiGD%2BSHErjKDO9Gy4va8yzZ0vWIChb6lwz8iKx0ovjfW76LFX65aTjwUI%2F8cVfQA8GujbkET0srTI%2BdTB8e%2FrfB1vO1e%2BABvUbO0ltVi1VIvj5I7SDsk%2Fg6gEKnyeICA6GfRMx4vMSS6QIBzcT2Hy3yQWGwQgdBC%2BRHvh%2Bbk%2FE&X-Amz-Signature=abb59caa1e1f7b2a1ea948175f3fd54e97316ef1aff332d6d7f450c52ff55b11&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGABESTB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC19SHLLTUxQ4c%2BmIHZ9YiK%2FO4pxl3mTPzdyH69Esi%2BqwIget5mROYTuc%2FAjIAMQ9K8E4218rLmD7%2B32TmwYkG823wqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZv1kiK1swamgnKIyrcAzgr%2BIj9CYgwsyG9TFQB8Nvh9W9VTJyExnt3Xtr01RRdWTDp2gjXXhCNB71fegIsP%2FuT2Q%2BoyyHWAbwSJnpsnoGnOOAwCheItrt%2B%2FrSNAGpzZZfS0bIIiRhXn7X00lG%2BMFKUPihtnQ7I%2B8cV7OUqkSG4YlTCUVjq8xCMAV%2FEvt10cIslQx%2FbgXArILftKfJApHufTwW51OCMCOZEWANbLK8WR%2Fos%2B3LgqQGWS%2F%2BtLCsP9e%2Bgl6UvMKfChlcDzX9zo3OTzO%2FL%2BPj9gA7OqumT3bkEAmHB7BA0EcMRHez4Fy%2BFs2ZcehdVZKU4HHbd70x4zuPp0QhZcKOvLAuzwDA2GmW5X1Rpki82AH2H9HluMDouktd3Z%2BiBxYF0rfsCx%2BSsC5%2BLwwMK8taa48oBP3Ip0Vrbuak5p2A4vd1bJUQYY8t3b%2FGaUqLv6zcnzO5JwiBFOyx%2BsbS3LleT1mdEk4lfemr60OCR1OqUrwG5jrMOaaI8lPUNcqUOJtx7bBqibz3TQ3clHiQIW0bAYhwzpKOcjrAlEYuMuq1T%2BqVARsTKZdl%2BVYfpKA3698tuyw9hbRAmlcVLQvEnlOS2jmglqEaK5k5W%2B71wg2KFDPDI933hP0ScmHO3o2iDxr3OcwXoMLDd9rwGOqUB6TEzA1HUgkoAzT55FI0OXWLwkRVZY1EfuG05Z0qwDxf6zasXTITiGD%2BSHErjKDO9Gy4va8yzZ0vWIChb6lwz8iKx0ovjfW76LFX65aTjwUI%2F8cVfQA8GujbkET0srTI%2BdTB8e%2FrfB1vO1e%2BABvUbO0ltVi1VIvj5I7SDsk%2Fg6gEKnyeICA6GfRMx4vMSS6QIBzcT2Hy3yQWGwQgdBC%2BRHvh%2Bbk%2FE&X-Amz-Signature=150cea6f81b92570decda3173325032cc6f22b756ce82d5e4b08da2e194e378c&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=dbcfca4ed9a9c5794a00a893822b9068c735e45f4499a68ada664d6cc78bbd6c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=673fb05319f19185a220a6e89ac57e46f4f81d024783c2ee6896c2b27f416789&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=3d86c5b7c8197bb14b5ad476a4ff9962b8e84740e9a2ade2450c9808dea7b91a&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=1e4154d376c33bedacb10fbacabf3e7d43ce6768d3d9cfb2f02aad62fd628d48&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=5f077e64785d00987228eca40a9a7504d9e90ce32ff03679fbbb7b7cacd2f4ac&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TWNSTU3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBwZmeqLFgW2Z%2BG3MHHT2dN1ptNUwYvfQSOMBVb3IfUAiEAnrMOY4%2BBglGvFi777ORS6GZb9%2F9QXHE1p6%2BYKZ%2BIG4QqiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDuDTdcLhAD%2BhAWoircA4EJaPdWcV2cgF6AHQwfFs7PPWxpy%2FGWe1tH2ivXZPWcyNwy9HtVgoXxorXnjhwOovlcb3E%2BkeKSuCCBoyU76KZ5t7nYNaKqbI9VTNfRc1YLwuSJBlPkZMHH0bm2j6OHswS4qzOlQ5DZTiks5VjvfZPP4O0DcN3iFjiVeBgHlkwBMBOxb08K31OHIF4DeEgQAKwD4OvS71hQG4vcPUPcpkfJV%2BLfO24P%2FKDU%2B9IUoFL%2Bvp4qkkfHA8z0r7bFTOp%2FWymQDP%2FvDhg3lXr5iREFjVUM6NG5lhSgH6ykG%2BEDvdicPUOoofNQluNNFiaMBFAcrNX26FU%2Fq9XWMDzVTHccXNCk%2B5eNsZ7yKAlDDfleS%2Fn1tMY5ME3fDh%2FTcEL%2FLe5pajkcSm5dzJHdT2XJ7RgvrQ%2B1iTxs4NlCIsyDDdlNufiD765EiEaRUv%2BgmYk%2FaMKsUDt2c474zA8ddL7BuKrlZxtK1K54X2BtRzhBbbjXXP6snLQ2oTFhlV%2FUWSBkWgSTgorol8ZBGhWK12t4g91cLAhkfJd4DWB4c%2BKBgrCWeNHYnHwK06xedhx7NemfDRca9wyVPdX9xZpYVXRMzxcN55gpvOcTGA%2BAz9BuD%2BLrEiptvLf7SNS45ME1AmTEMKDd9rwGOqUBNVTJh6726nZOMpRSqWDOc72qLpkVl8S2YnpFH0CyUOFb0eOmoGpHJ0CY4PUmIa%2BtSaFfUNZWw54VbO7bxXbzgKDGyNlPNbCjjlzGEs7LwDcqwozipuTzQA6xGaUnOTq7NS4HNaL9ekuErq6i3mXfouFcRTD4xjJLMo8dSCpYedvmpUehP%2FV%2FOuPdDfRy41fimWtP%2BlvQd%2B6F0jTm20haZIy9sJSv&X-Amz-Signature=de5a68a32043166a4629aa0975f8e1685853a81d1b2372ebe58f72fbfaf18db3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6RJ4LG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQRXXkhnafqSNcjhpVdrOnBxrehPShztnd%2FmcW4LSCAAIgfFGey8x0VIjYUQBwpEZKx7e3cG4Ph9R7cjG5HYAnyu0qiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDENW8IrhRTvZESNX2yrcA86B5GIbhRAySSYfF%2FcDjqZsPRFSq6e%2Bk2S3ocPPzsbNE%2Br0QfmhNFuYdBCtCB2ufYVNhJrBXYHKCx8MpWIuRPEZXeFxGpiapUuaFs485FnBHATOW4CMY1178wlTB2m%2FnEO2cS%2B9IiOtIZ9UyFEB4O6Ie2l61Fd3hzG2BHcdM4rWK5bcbaExG88LoVrEnxm1b0fGhReLA2RgKE1SnULMyySzjT%2FBIv0QpJUIyTfdfZU%2FJtBoZZPYvMXVP1YCv%2BcuoAw%2BcKgXrVUz%2F9TpE4j6ODNWKgmRzfYUI694TJ3VlH08JabpfaxbwNmYzAktljg32Ryh%2BK6KIbtTQl2lm1dkWSPhO6lsBb92cTTn6bd96B6DwdeOTndBWDZX4nUtiNASI3vzfCbGtf%2F7YPwrujiKoOvZto%2FNsxrr5HSGZdhQWQXHIvT2tUqA3MnXEaPmpC11tflGSG7G2ThOkymWTP71MyRduHd7zE7du9QbPdxnGVoW9UhiC14akBOacA6nPVGdLrGknLsoe2HWzrk6vfJD3d1HNoUpOUWUgWwUoi75PMk6asMmQ2oGwWLqWUwoQpfv%2F6ANe8UXy5Eyo9CPV0HPJyTKohPcoDWOCugIvb9WQPshWiJUv0YLynwCzosdMMjd9rwGOqUBZf9gE9yCJxpl5lQGub4Pujcn69M4hpsdnDKMy0AZV05jgzQ1QeilmNZNU8QruBXq5cOn3cTFZFW8i0ZW%2FeuwyyZCdLklI%2BS256g3R9fTgmI0RymknWUUSQDdUHDJBFXKLL6OS0p3EBEZZBAGC4lthrY2UHSfZyOQhDcmaaaNF4si1UHG3UAv39F%2Fevsh1%2F8g4N%2B8hd3E%2FNbWDpf%2BSzum3KyNpKwz&X-Amz-Signature=3ea7639d496ed8ba462de2cfd355549881ba8fb56cffb6c3d03597cb08c19477&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZH6RJ4LG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQRXXkhnafqSNcjhpVdrOnBxrehPShztnd%2FmcW4LSCAAIgfFGey8x0VIjYUQBwpEZKx7e3cG4Ph9R7cjG5HYAnyu0qiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDENW8IrhRTvZESNX2yrcA86B5GIbhRAySSYfF%2FcDjqZsPRFSq6e%2Bk2S3ocPPzsbNE%2Br0QfmhNFuYdBCtCB2ufYVNhJrBXYHKCx8MpWIuRPEZXeFxGpiapUuaFs485FnBHATOW4CMY1178wlTB2m%2FnEO2cS%2B9IiOtIZ9UyFEB4O6Ie2l61Fd3hzG2BHcdM4rWK5bcbaExG88LoVrEnxm1b0fGhReLA2RgKE1SnULMyySzjT%2FBIv0QpJUIyTfdfZU%2FJtBoZZPYvMXVP1YCv%2BcuoAw%2BcKgXrVUz%2F9TpE4j6ODNWKgmRzfYUI694TJ3VlH08JabpfaxbwNmYzAktljg32Ryh%2BK6KIbtTQl2lm1dkWSPhO6lsBb92cTTn6bd96B6DwdeOTndBWDZX4nUtiNASI3vzfCbGtf%2F7YPwrujiKoOvZto%2FNsxrr5HSGZdhQWQXHIvT2tUqA3MnXEaPmpC11tflGSG7G2ThOkymWTP71MyRduHd7zE7du9QbPdxnGVoW9UhiC14akBOacA6nPVGdLrGknLsoe2HWzrk6vfJD3d1HNoUpOUWUgWwUoi75PMk6asMmQ2oGwWLqWUwoQpfv%2F6ANe8UXy5Eyo9CPV0HPJyTKohPcoDWOCugIvb9WQPshWiJUv0YLynwCzosdMMjd9rwGOqUBZf9gE9yCJxpl5lQGub4Pujcn69M4hpsdnDKMy0AZV05jgzQ1QeilmNZNU8QruBXq5cOn3cTFZFW8i0ZW%2FeuwyyZCdLklI%2BS256g3R9fTgmI0RymknWUUSQDdUHDJBFXKLL6OS0p3EBEZZBAGC4lthrY2UHSfZyOQhDcmaaaNF4si1UHG3UAv39F%2Fevsh1%2F8g4N%2B8hd3E%2FNbWDpf%2BSzum3KyNpKwz&X-Amz-Signature=81417bdc748d346d37f75bd79e71c7201c0a751eac351103deb55636760fd3a0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUYHY4QZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCphY2e%2Bqw1rm7c7aU49cWoou9l4Zaly9N%2BKesGiUIkEgIhAK16jVkYikmD5%2Bjc25p1wQGzBP9u%2FJQ1N3471AlkubHfKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWQyhp5El4L9nyjRIq3AOUU98c48cy56y2d02qheOvSODdwoQHEgPu0HWnwJFz9cWXTLgrUnU0PdmMxv8HEa8JO2oEOdDd%2BucTUvmFp6aOb2s2bMwi3Uyc%2F4O8OmA%2F0qpAI3fS3dAhnWJLhmmIwYUJRG2nXgxFsma7s8PRZbxdDNhCSjrzL4APshXRq9IGfDKP3bkt1V%2BK%2FZtTKh3tEukuo51FCCq0rhPL%2BCx6IikHY6ytB8RI%2Bln%2BSb1ow7Ai9T6LIErKkLdMVXDHdLszmQbuIGsYNzBgRMpB5FucNijscQKwVjr%2F1%2BOoyi3w6OUrrePfDfnvkyNoFQttRO51p2Dk4E648Dc208JwUF4sBzBgC6nbeDC5zup0rGK30PPloFez7x5pCY2VMJLvunurUTZaiTWbYbhC92etAMohPScqkePaiIYHs3tdW05RwoDJqW9WcViTuwuAWy2kWziI1RFC2eYgXH8IMoYhTSSNG4%2BG77nYEGxMgnqQrT348Ijot2RwoB9%2FMexZOM3WOIP97QDE1ylSOFXkQ0rvCNO5pAQ9MZz2zZ6bgK5gd7DB2sbBLaCYPZR4oOObPkxOo6Ysbg1U6zsHo8FjE3Tbxfl%2BfPGiwEZIuvHg7cMac%2FixGRXZIWTx0fyH1G5%2FbI1yaDDX3fa8BjqkAfVHn8PhLACZ7g4whI7VkuVB6WneqpWwUGRpF6vxfbdmPgyB26n9y%2Bbqi2KY9VMWIB%2Bpbe8JNzrRrqGBiFiXELYwAALULwSKSa%2FbizfdJvHweY529liNHF65%2FOSxCTTSfkfGXpw50MapKfu%2B5NysdKlp%2FhugSmR4TgHWkORhb5apVavVoDqZHI03FnBDL8%2FRiQXj44rHnZhFye4wPq601%2Bo2dQzj&X-Amz-Signature=947bae67abb2e8ce2338174c87b38d67d3867e36b7867fa419f0a443d4becb35&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QNVYADD%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T061916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1x4p%2Boqk1%2FpewYqqXNxenOwhtrBAWS0GkVK%2BJE2PYjwIhAK73035NYeAxcbekIogIZlDtrXbdUfVeNlcxR6uaq2DVKogECM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNh7XSAc0WkFEJET0q3AOVAtwpJ9FgZshuYPSkkTwMGF5FYzXjvUz3LcfACYFSkQi8nEbvS2mLQorM1jGrwri1OwMV3FJ1PJ4FHxIAeu60m1M5xwRc7oNo9PCa0pUCiyy9IBxwIbCOvvFgH5RiOpXFNj1c5hO98Uf2liNqPS6KcYbEd7XF%2FNmt0rRDnvhQpmcctlGolQYfOdVvEZgsoQ1s7v%2Bx%2F9Mhqn2UnofVwDx%2BCBas09Wr9sP9SL%2F89FrdUuQTZvji%2BVFJXyQN%2FAYcAWMXaVFhkp83NKk4AWTXkitGspvNAHBMyqwOpw0vz8DaeqgWl37yO0mqM1wwlCNcQdlW97HeKSnGSLjAPYU%2FYfdYByaXrsqFT7mq6puEg2sEpLlgQ6%2Brtzg191aEkNEbdUGU42uMZC8bjd2%2BPXqpbvqbBCpiINC7JHbPM6HiifO7oKSzteX8MLOE6NmaHI0PCDMyolwXqtgVacAh%2B%2BO%2FMiRfO%2B%2BgbeKrTyHFNLQzAlF6osu0BEUol6yH8siCvos6Ib%2FOvj8FoksIWU0zpENFMfwC8fNpHIohmO8o%2FHb8w7A8VXvd1mKsEWhygJMjrcIdpo7usmqwqmwCRNCODLcv2jDFsENOqNkfUERnlAcAAlm8%2FOVTILFgFb2y4MwoRjC93fa8BjqkAewB2SEeeWoKZwwt6IKG7KnLJxpqBcOG0RP8kvGgDeebn%2BnESJg4eNO5xe%2Bp5mIVOKon6JqdaEF7c1mkZyDl%2BJB4wc7nLK6kLZlv87zmE6p0YnNdgH9rhV3tfxmlqn%2FBHLKKomMPT9OLnKQLWUZ8ztOaREFGaWLhJWZ4hcaPBZbdIwj5LtcqHSi%2FHI2qkSGeXzivn4zqcskzlh9rzKpAh%2BDeUL4n&X-Amz-Signature=79a83894706629d8d44c1a2e25c0d36eb3a40a07aca9707ac688fcce76012d96&X-Amz-SignedHeaders=host&x-id=GetObject)
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