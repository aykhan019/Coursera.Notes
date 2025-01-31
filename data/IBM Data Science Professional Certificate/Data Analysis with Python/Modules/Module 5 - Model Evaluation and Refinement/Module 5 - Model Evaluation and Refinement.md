

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=aa631e4f5885bc455ea0cf5770a389ff11cff989896ca8f4c4c8bae5cee09ead&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=4686f29c09a000e12b83daa28a99df4c998954a6dd01a72223bffd99d83caa77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=436d1798424b40fab45fe40b3f487274699549ce373b277a197f0705e44281d7&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=dbd86f49626cdead231785fc25ad94530fbf03ecf733b92a75fc3d5e746daeb7&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=1403f61ac3ff2f365e3a4cfc63fef7ce2c349ce1c9dd3326682ae531b1e10f83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=71b563f7f759424b1be5d2d74602492bc6b012dcf91006000359b986a6749d5d&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=aafb49a897b8b7f3d4aebf4a58254508c38668914168a4d3b1e332e84aea1e0a&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=0d5ed93c12a4408f9c272a800a903a80c203481526973950ae1370ed56607fa2&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=3e08f3c199ad2c0cec40da456f571bdb3781131b4ba647b701a267c523a0b3b3&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EJNMSEV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH00uINIyWA480mvTtz7uHGZBoTjKPJEErsUdxazAJ1vAiEAy9rQeKoG0p1kQk2pjEvvitXIv52jr7AJQV6FCoSTnF0qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL42db1c0nM%2BLOTGKSrcA3uQu3YrpZVjGNOTMyyzyq83TCTITTCT4%2F3JTzjXKthfJMnyXaeurw2mt%2BijGblQwWCpcNQlZRn6pAhiy6rLf8RXZx%2FJoCkQdKfa4N5S1BE%2B8iAL0a%2BQwErewFsfTDsa1%2BlEBlf9p6o0Pj5NRDEYwGmqptV1LfDp97QNCgRpFZxfIXRPWsokD04izoOsF9pueNmUwSoNjVgpErKiGDjwA6Mka6OViYVj9ZjDwy%2FTTegVlvj1OzY2t%2B27aDOGKfOXzCcBusRJD45QDbnayy7eJ5K0zkaWL0s2PpS9YExazzrIRahZAEWqrx4YuzdH%2Ba2Sbvt%2FNSVCZN%2BfWorcg1kL72Nv4HKTjwsSKtpbGtScKsByn1Sg4ea6te%2BfYExNEuVVeUekHOCSwNbQSu%2Fm4aspxokzkjjJ1cKXjw1xpcxptv6x8YrXxXkePtYT6MQ0EG%2F6WseUi9f9QHoPPBnZLIBzvHGwDf2nNnd9D%2B%2B%2BQiSJeRDn9vFt6%2F9Iu%2BuMzGysHzqrUcS8s6S7tPncowNWMVzA1qw2r2FedwY62%2F7EwqiXvjf3WPvAV4IZr3Mboul2CEC0SRhmV1JqqZx0aWyrJ0ZVeUun0LJIWno7SdfqSgTFRoLgEooJGmXF3WmNC87kMKLA9LwGOqUB%2BUKw3CPwSiy8YuDSkO5NxI8HKnPICeRMELlVy1KDANtnbYlgBV4hpKEnoW%2FyVgaIFN8hjBK60hRkYfunV2LsWWcpPiZE3mAKaIIQb9PvjiyWd49%2F5HrKQELJPOZywzZ0DZPYCYMsO0RvWJ1tC8ZxnNdH%2FDEplmynOYaIbhdwRst8UCkAD0WzctapwxaTXFFnF8Pf%2BG%2FZeMjLK83gRTeojdJDjcaw&X-Amz-Signature=fa0cd7483701743562a04f9e8f60a31f29966ee45c223360d969b2f85b101e20&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EJNMSEV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH00uINIyWA480mvTtz7uHGZBoTjKPJEErsUdxazAJ1vAiEAy9rQeKoG0p1kQk2pjEvvitXIv52jr7AJQV6FCoSTnF0qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL42db1c0nM%2BLOTGKSrcA3uQu3YrpZVjGNOTMyyzyq83TCTITTCT4%2F3JTzjXKthfJMnyXaeurw2mt%2BijGblQwWCpcNQlZRn6pAhiy6rLf8RXZx%2FJoCkQdKfa4N5S1BE%2B8iAL0a%2BQwErewFsfTDsa1%2BlEBlf9p6o0Pj5NRDEYwGmqptV1LfDp97QNCgRpFZxfIXRPWsokD04izoOsF9pueNmUwSoNjVgpErKiGDjwA6Mka6OViYVj9ZjDwy%2FTTegVlvj1OzY2t%2B27aDOGKfOXzCcBusRJD45QDbnayy7eJ5K0zkaWL0s2PpS9YExazzrIRahZAEWqrx4YuzdH%2Ba2Sbvt%2FNSVCZN%2BfWorcg1kL72Nv4HKTjwsSKtpbGtScKsByn1Sg4ea6te%2BfYExNEuVVeUekHOCSwNbQSu%2Fm4aspxokzkjjJ1cKXjw1xpcxptv6x8YrXxXkePtYT6MQ0EG%2F6WseUi9f9QHoPPBnZLIBzvHGwDf2nNnd9D%2B%2B%2BQiSJeRDn9vFt6%2F9Iu%2BuMzGysHzqrUcS8s6S7tPncowNWMVzA1qw2r2FedwY62%2F7EwqiXvjf3WPvAV4IZr3Mboul2CEC0SRhmV1JqqZx0aWyrJ0ZVeUun0LJIWno7SdfqSgTFRoLgEooJGmXF3WmNC87kMKLA9LwGOqUB%2BUKw3CPwSiy8YuDSkO5NxI8HKnPICeRMELlVy1KDANtnbYlgBV4hpKEnoW%2FyVgaIFN8hjBK60hRkYfunV2LsWWcpPiZE3mAKaIIQb9PvjiyWd49%2F5HrKQELJPOZywzZ0DZPYCYMsO0RvWJ1tC8ZxnNdH%2FDEplmynOYaIbhdwRst8UCkAD0WzctapwxaTXFFnF8Pf%2BG%2FZeMjLK83gRTeojdJDjcaw&X-Amz-Signature=0fc15b6f11883126759a8ed3b7835124aaeb9fb1514652766875612fec2c1942&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EJNMSEV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH00uINIyWA480mvTtz7uHGZBoTjKPJEErsUdxazAJ1vAiEAy9rQeKoG0p1kQk2pjEvvitXIv52jr7AJQV6FCoSTnF0qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL42db1c0nM%2BLOTGKSrcA3uQu3YrpZVjGNOTMyyzyq83TCTITTCT4%2F3JTzjXKthfJMnyXaeurw2mt%2BijGblQwWCpcNQlZRn6pAhiy6rLf8RXZx%2FJoCkQdKfa4N5S1BE%2B8iAL0a%2BQwErewFsfTDsa1%2BlEBlf9p6o0Pj5NRDEYwGmqptV1LfDp97QNCgRpFZxfIXRPWsokD04izoOsF9pueNmUwSoNjVgpErKiGDjwA6Mka6OViYVj9ZjDwy%2FTTegVlvj1OzY2t%2B27aDOGKfOXzCcBusRJD45QDbnayy7eJ5K0zkaWL0s2PpS9YExazzrIRahZAEWqrx4YuzdH%2Ba2Sbvt%2FNSVCZN%2BfWorcg1kL72Nv4HKTjwsSKtpbGtScKsByn1Sg4ea6te%2BfYExNEuVVeUekHOCSwNbQSu%2Fm4aspxokzkjjJ1cKXjw1xpcxptv6x8YrXxXkePtYT6MQ0EG%2F6WseUi9f9QHoPPBnZLIBzvHGwDf2nNnd9D%2B%2B%2BQiSJeRDn9vFt6%2F9Iu%2BuMzGysHzqrUcS8s6S7tPncowNWMVzA1qw2r2FedwY62%2F7EwqiXvjf3WPvAV4IZr3Mboul2CEC0SRhmV1JqqZx0aWyrJ0ZVeUun0LJIWno7SdfqSgTFRoLgEooJGmXF3WmNC87kMKLA9LwGOqUB%2BUKw3CPwSiy8YuDSkO5NxI8HKnPICeRMELlVy1KDANtnbYlgBV4hpKEnoW%2FyVgaIFN8hjBK60hRkYfunV2LsWWcpPiZE3mAKaIIQb9PvjiyWd49%2F5HrKQELJPOZywzZ0DZPYCYMsO0RvWJ1tC8ZxnNdH%2FDEplmynOYaIbhdwRst8UCkAD0WzctapwxaTXFFnF8Pf%2BG%2FZeMjLK83gRTeojdJDjcaw&X-Amz-Signature=f0e6fafc66ffdf56d2d33b4e4c76b8e5058869f40d9f7fa63bbb6ad9294d6e9f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=429a62d8d9bbeb9126448c16e10d47e2eca076034834ecd1c8efb9a0a5f99457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=ee00ac1bc99ea14a18d77f3c37c8b981dfb01f933b02bf0101f67e3075c9a5ad&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=3d990ff628f4f02d3e0a2dbb6db94200a20ba2a44bcaaa80739a2851acf6644e&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=54e0772b5a34f9f8a8bae8bfb240e356280c30ad612933f5d2b9ef5f81ce063f&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=381a6216288f9fbae3229f46ae9bd15f5fe1fab48bc7e94007854ba624aa3386&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMYP6RGY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHYGY2%2BvT8INn%2B6o4fDZfd%2BqbAOwY%2FLXdA%2B4IL5m8iIYAiBi0ZpXrsl9MoGljbVuxzK%2B5%2B2GmWvFpyKs4u90gWboRSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2B0jhxN8IcM72xDNsKtwDJb5K7KuUvU0ApAmumaaMTW9eeVZae3RPzTkqNf8KGkG1cCxKIUBGjVzyMIatABUBy06gNsXK6RvHP%2FJkD1oqCrKLuCdQIGIE7jaNhXk5d2D905OL0QO4haeSHYkKAGFYHQVAzZlKzZ%2B9XRLcTdrRp0O3UzgfWpYPi1%2B0SzB2P6%2F4dczZ0dLwTbbhI7G1v9Yofinn%2FWU97iOwKdco3GwnBT20%2ByKx2jer9dbpGvFM2a4bksADcMLj%2FEVxR9oAcjMpj9xYrnTbRxNZTc91KbEp0G%2FPBkY4VUXIWALhde1QBaUfP00FWHkUYWIkQ%2F0AbQFe7AehQIimO%2BGkFI2MmbohsABcbBo0qYdlUL80r604wtchtD0YHSn%2F9l3l3lk0AkNXSJQreyQIpu1UyhSokXtkKGaMqu7XZ3SRugGW47eXQJDessVzXZY65YkYLXaPN%2B1d2xD68dkq02mV4c20rbuLY9y2gONXNzMMQrBNNfQOCjZKwMBlE3cRfvzhqVNXTSzJbVplZiMgIsyL400YJEnjKnfftx74WjNk5DKSnGcMIaQPqXOEnk82Cugxsjnz3ybefqXRs8kdbd4AQzuvAY5zPg9DNkymNKhVSq7LdvPsnxzIBe9G%2BvLegGiApqgw87%2F0vAY6pgHVngmThdVNcbdGUfy7KkHA%2F7CSZyeWmyGwVsRATU%2FmiF%2BNJFuikvWL1dDez2F%2BaBlveJZ1euFLQJzYi00ocmOnlEVu79rsyr1bi%2F6JnXAS9Es8wFuHOIR9mlhPmconRcUd1oVsaDkFI%2F2Kf46PguL0BCN0ig2U9U6irKXVFZfJfJhWswGOAIae5WA1O7d%2B%2FKNybT28r1ki1KUw80xvEdkBFUqeefg9&X-Amz-Signature=f64c00fb88a73b349e723a96713bf9868d9df25487eda02c7bdd8195b28235a3&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIG2DTAQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDicgfkHd0mEBdyoaR0f4i9zmr5RlB8pUJAtaSBhRCC6wIhAKO%2Fd5D%2FYgXfWpIqW6PnxSLi6RcvdwkgBll4s1j66UqVKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx2adA0mXr9zeodxoq3APZOAcrqeUgdGdQEWnLmB%2F60I8rFdsQ2lTaxQIrKIjQ3v5mlqwcWOXEYHvl7XCw%2BzAp5CuGKzcZmpT2VF6GN2KJph6sQ53KE18MsFmK9gEK2qQJcaymzDcQGLR%2FQF2MeLjgQ34asvqIXj48rCbWUtLtVf13Whzm%2BsWMDNAfKCH5WjzMz%2FcLaBCsYXqHB4BgnS1%2FoTvjBpf4rziMUgKiFwzC%2F25qEZM7ewptsT7iGGpYYFAW3TVM7MKDtGMeCdCfpLvVzwB49pbwAr2qECPMDcna36OGzf4uYsNq8yXdpRBA5GirmaFuJTOgUVsGJ532IcJCC65jXfOebA3djFlZdSwlhh6HhtzBFSbwW88gBiRIHj1Imb3CQHz%2Bonfx3AAk8wsUyYlRJvyW%2BQEDqx2F912wJ48A0jUixz6GjQeYtqYeso3LkXPA5Zm9cfoipRP2ONL3NQqdRkqrtvZF%2FDxAxKRGlUvPl89tzkP44dHeiXmky8%2Bb6Js8Q1sI8b3c62pDmfbCY0ISkjPwBg27i96ZeSh%2Be2BEI%2BCk5dfGtp3NH4kq95zOhxnFWPgYph4WDNTo06TKjzsI9a0%2Bp3W9Q%2Fqgf4Z1DjUzgF%2FQP6Ax0yU%2FfTlSpEEAsOvzs11RtSX0qTCCwPS8BjqkAZZXtn6gE2xj3wluKZgsiFauhE143tleXbEY08%2B%2Bsg3oAmeCw3E9C%2F7qL2NhrgVR4SeM1%2FOBScnI%2B0v0xbIN5mPvMTMWSJwDXI5SGmpMAhtas7OgmS3KE7riU%2BciB51nujH%2Bgx2NyRFRcLiRG0QL7fpG%2FMBihuPrctz91J%2BvX5NzgUgAmO%2F1BNVWbBuLrG%2FNi2W%2FYu7wF%2FNulhrQ0N%2FFtjpDFMcU&X-Amz-Signature=83e605c461bcbe08cfd929788545ea1903d6d069928402111dc3be315ec4ef46&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIG2DTAQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDicgfkHd0mEBdyoaR0f4i9zmr5RlB8pUJAtaSBhRCC6wIhAKO%2Fd5D%2FYgXfWpIqW6PnxSLi6RcvdwkgBll4s1j66UqVKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx2adA0mXr9zeodxoq3APZOAcrqeUgdGdQEWnLmB%2F60I8rFdsQ2lTaxQIrKIjQ3v5mlqwcWOXEYHvl7XCw%2BzAp5CuGKzcZmpT2VF6GN2KJph6sQ53KE18MsFmK9gEK2qQJcaymzDcQGLR%2FQF2MeLjgQ34asvqIXj48rCbWUtLtVf13Whzm%2BsWMDNAfKCH5WjzMz%2FcLaBCsYXqHB4BgnS1%2FoTvjBpf4rziMUgKiFwzC%2F25qEZM7ewptsT7iGGpYYFAW3TVM7MKDtGMeCdCfpLvVzwB49pbwAr2qECPMDcna36OGzf4uYsNq8yXdpRBA5GirmaFuJTOgUVsGJ532IcJCC65jXfOebA3djFlZdSwlhh6HhtzBFSbwW88gBiRIHj1Imb3CQHz%2Bonfx3AAk8wsUyYlRJvyW%2BQEDqx2F912wJ48A0jUixz6GjQeYtqYeso3LkXPA5Zm9cfoipRP2ONL3NQqdRkqrtvZF%2FDxAxKRGlUvPl89tzkP44dHeiXmky8%2Bb6Js8Q1sI8b3c62pDmfbCY0ISkjPwBg27i96ZeSh%2Be2BEI%2BCk5dfGtp3NH4kq95zOhxnFWPgYph4WDNTo06TKjzsI9a0%2Bp3W9Q%2Fqgf4Z1DjUzgF%2FQP6Ax0yU%2FfTlSpEEAsOvzs11RtSX0qTCCwPS8BjqkAZZXtn6gE2xj3wluKZgsiFauhE143tleXbEY08%2B%2Bsg3oAmeCw3E9C%2F7qL2NhrgVR4SeM1%2FOBScnI%2B0v0xbIN5mPvMTMWSJwDXI5SGmpMAhtas7OgmS3KE7riU%2BciB51nujH%2Bgx2NyRFRcLiRG0QL7fpG%2FMBihuPrctz91J%2BvX5NzgUgAmO%2F1BNVWbBuLrG%2FNi2W%2FYu7wF%2FNulhrQ0N%2FFtjpDFMcU&X-Amz-Signature=39e36cf55abb5a37a323639960bbab5c0a7bceba70ebe0054ac9d142cefaa84e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SPC7EU5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGuAzTML51fhNZTGVF%2BxuKL%2FNQ6PViyy7DrcJcc%2BI0wqAiEAsLfVknQcydYbjRufJeKtyGwU6fzcYYnE%2F8q1T6XG2RgqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCOao3HvggK58%2BrpYyrcA3rEqKzJ4eLOJSAx7b%2FeUgtN3oxGlD1K8Frp2ZX1P%2FYlRdjkvanpX12HOTPQLwc9p%2F8vfKz67%2BNanRWccq70dQCbrYOJvtAtoV3qlP6D%2BydXzIjV9mb1XaMmtj39BW9k7uCzaiAS8WzScjgxQc7%2B%2B4PCxHUAcT24BE7%2Bc8sZc6lM4DfQXauCtX7VVi%2BkXCiBALSBXtli1OXONlr6eJAs0Lb2NAIE3JCOk9NiYQQcFO4J5pKbG42qTKWr5BKP%2Fp97lvm0p4ddhQwiiaKVB7hrzPdXMETYuU6oDx6VWNIdC9PS6lBeAl%2BRmKNwVv1z6q5PSOF4%2BH05u0AdyW3Wo%2Bg0abMFWbI%2BHLZRT%2B4FrgVPOUYt4dhgc3I3EEI0Xhp17EF3TJjeOwwINbR99RQ3qtzYybRYE9toR2GVZFsykNEKrlKr%2FUb7bWVYES92g%2FN3w5deLcbNYrYG%2FeAY67d7NUvcrFu3XAmrk4POAL%2BZIX0sn3WhYBQDkjGFTzakVh8n1eXKLB7k9vpU%2BIRXTAwPxxhu4YmzMiiOM7lnVNxcitp4NCiBfMLDr0DzlvGwVQqhmzQBohpKNbn6FfygMrcBTD0BxN0W5RXKIEqi3y5fu9q0H9zFAPAMfAOSOjGSaPEIMIPA9LwGOqUBo4R%2BjnefBDLIGDeBbSdoTPbzNGzgPRLx0t6G83HkZWrs2QZYXoaBHyNBLo3ROYLjvkfFPa72d8uNfa7ivDty2upI%2BEWG%2FFaEk%2FuXVLvL1sX1D%2FLIMmtcu%2FbGu5qqdFjEhti8jEmyeiFMz1MuSO3GB9l%2B3QvacLdWjzVb5dRe51YbbjhXTRxpFsCMDbGdehxx6N55eKVL1krzD4EQNEqbIbhtsdcr&X-Amz-Signature=a7ab385c42b8346e46ac0a919da1991ba640436902e86fcd93d1094060b9f8d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YIWMLUF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChQTihNEj%2FPODzw%2FFd9Muy%2BfgjC3kJS%2Bwmn03qJ%2BjY2wIhAPZumRKX9Ni2G3F5WP0XfwPYvRbGd7FvFyD0zSDaMZN1KogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztevD0fI4BUXuVNI4q3AOrfiou%2F00UdIJcgzjkzomGoWB4zyXlbw45PJ3EnSEn0UEzT7DN2htcDsrsUjoJrWozcKKAJgK%2B8JMo8xPrRJMufbzlREl%2FtHkOFgZqByabdp7jhRxbho8YKRzQi0KGdu1%2FUkL471MLw7BTOZktq7OWTZqIM4XP6aSMtKe4AQsHAHF0Ybsl4qZrmZSxhgN5mLUVy77ntZVR1iO%2FCUAhlbE6WlaanZFy5B3Wlcmr7g8Igua1IA%2BkGotTV%2BVjdG48e8ztyVfzfeXd97F2ECc%2BJQNk%2Bl0KAM2zwZnSeELAO33kMgPTsDVV%2BcH0cccgPNSkXOZ3%2FRMtQ4LIDOY5SSFT6bcarxrsBPSPMyQ7HxS3LFWIbi8Dm%2F0qyKRtV3aDBuMVg57opjEUrPVTCOQvEIajmUl2ofuQ7j%2FzlWshwDyLaOhCpWWEQr4kZX5mbOK5hC7l7jhgW3FuP4NuydnTs%2BFvFNprX5FICvn1i0UA6BsdGllAzjCeHuC4sQHZKTOpaOyLNcEOyP1ES7BduuFlqMODqlRl0KCdCql5PiLo5yNXIXlfjnpxR3Myw5qeVIuzrZ2xZzXjl%2FGM4IjWhz6vWTdyvmZPbMtgN4E9q50cEv%2Bpfz6tGg2dG7ZaZyGyWUCrGDCzpPS8BjqkAVP84UzDNbEjbYHuHoF3hKs4I%2Feu8XORDzGK8rHnkLjisqYbe6tDeD%2FLyt0TSsYoN4MmKDufCsuw1QfCLYs6kUTnuaMj%2BTvIhjVUqKvpMlHEic46cBZ8q904PuO%2BNY%2Ff1Y60Qiy3l%2BnhpbgUBXqiBaVsiDu3sz1EzG27fr%2FOg%2BgNMeRKA%2BiVQvTWvvs76dyf%2FeJK1wZUF4UTSzwdxODV1b%2Bh3UiU&X-Amz-Signature=237c50de784a4c71bc0cbcfcbc1f8918ec023e6350d802fa582240bcbb47db5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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