

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=ed9fe2edfba2890cb883f671814a1a248ea17d65f7ee77a04197ed98a75e6cb5&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=3583efa25d42ae75ee6aa4f2298318a56170967d582ccefd0a0963569cb0e004&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=dbcead042f9b9b46fc49d16c5b5094cdf277fbc7b82be29ed152c8baede8225d&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=6eceb14d533888dd8ff547f6b4e6c2e8fff750e00bc0493bf1c1529580268358&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=4a0018214509a5cee58503ddcab0c8e814772b5c5f4d7d24b46d3394874e81a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=d58a053cf9b759a05f634fd91ace82d7b2fae226f0208bf060f3f81f3247d9ad&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=4525672e2b140a1827d7c3b17ae9ea983ca6b57e8f192728ad01e9ff732f4a66&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=e725b9463f47079e1821dcbdb2f303ff8a77de4ffda297693993eebb96c9278e&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=d6fc47460ab655b8a1691e263613822490472170e323d90859cca1361bdbd908&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU3WAEVE%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIE96vrNtd7Arp9iE%2BSXd1dgePyfSfb5A6Gl8iYAlkH%2FUAiEArZnMgFIq%2F6zY0psOvZNCXJzJR09n2h9POGrL2oH%2Bu4AqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0YhzzVekH3ZpUHRircA4iAzo3pKUUWptl0yB7jmjxptdoId7neRA2FWAbOR9H5Mz5R%2FYh6ExD5BVum%2FtkxGG4EPp%2B9RJOriEs6MYZYknXTmhoVKDnVDEqiDMAHzCBL5It4zyJY3MfPvNWcOSARNVRLSbje53E7yM6u4wZS9%2Fe4Ip%2FMnB5bQ4P6L8FgGBtchbuWwLvD1lNx0HiSb%2FgD8tZXgnTFFKaAgkUjD%2Bb%2BS4jcMMKSyqLx25LMqMDVqawRV28YviIpnaJ9p7uDn0eTrMD9nvPuxvi6oCRruVKYrOz%2F3SX2oxseg6oExprTCMuXvX0L0dzhgDujHmJp9rbaA5R90lbeqRXXp5k66oYiselPRwCRaE1iwzEeR1dFIr3SE%2B8CwFL8Ldhqtt05wZCMoXkUd4ERPBxrEfM4vAGw6rQB33ZJujhHmkLk2Vx0tG1aQ9f6fStu4zV0Lg5xYxqNIb8K3lTbQ335BUI3JKEEvcT6nzn3RQAoLBYb8%2FmfMe24FnEy3m%2B8FSnErJWxEdDaZIEA8kHdMFXgopnPrsYxxpcJdyElYv0Y5XF48D8o65yOBV%2BwC4AXO2fGfrXFuWA6REXlk4auWhLAZGwlk7k9MKEbgN8nWe5WtG54wnX%2Fx7lTKeguDZ%2BrkBUXy%2BY1MPm1%2FL4GOqUBx%2F7ym%2Bx2OFo%2Bf8QclZhEtlBnlfPP6u8%2Fg%2BPsHEXWrwGZ0BTN9HTShHvbnqKGdMs2yDkzfPjb%2FxJWat%2FID68rVhJVClmRX2v5t253VZg8Ob8U5CBcSaYVBUl0j0uYcbTy7K4fmX4aa7UwIYsK9omND3lOlXmfsQfhNGZPm%2BPmgY2lrIVH90pwGINYVyNPtL0TGeaHVTr4GZXISaO2FzsPxYbMr32p&X-Amz-Signature=125210d80be41578932c8ff3850ab120264672676319d7f599285d4ea3e95f61&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU3WAEVE%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIE96vrNtd7Arp9iE%2BSXd1dgePyfSfb5A6Gl8iYAlkH%2FUAiEArZnMgFIq%2F6zY0psOvZNCXJzJR09n2h9POGrL2oH%2Bu4AqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0YhzzVekH3ZpUHRircA4iAzo3pKUUWptl0yB7jmjxptdoId7neRA2FWAbOR9H5Mz5R%2FYh6ExD5BVum%2FtkxGG4EPp%2B9RJOriEs6MYZYknXTmhoVKDnVDEqiDMAHzCBL5It4zyJY3MfPvNWcOSARNVRLSbje53E7yM6u4wZS9%2Fe4Ip%2FMnB5bQ4P6L8FgGBtchbuWwLvD1lNx0HiSb%2FgD8tZXgnTFFKaAgkUjD%2Bb%2BS4jcMMKSyqLx25LMqMDVqawRV28YviIpnaJ9p7uDn0eTrMD9nvPuxvi6oCRruVKYrOz%2F3SX2oxseg6oExprTCMuXvX0L0dzhgDujHmJp9rbaA5R90lbeqRXXp5k66oYiselPRwCRaE1iwzEeR1dFIr3SE%2B8CwFL8Ldhqtt05wZCMoXkUd4ERPBxrEfM4vAGw6rQB33ZJujhHmkLk2Vx0tG1aQ9f6fStu4zV0Lg5xYxqNIb8K3lTbQ335BUI3JKEEvcT6nzn3RQAoLBYb8%2FmfMe24FnEy3m%2B8FSnErJWxEdDaZIEA8kHdMFXgopnPrsYxxpcJdyElYv0Y5XF48D8o65yOBV%2BwC4AXO2fGfrXFuWA6REXlk4auWhLAZGwlk7k9MKEbgN8nWe5WtG54wnX%2Fx7lTKeguDZ%2BrkBUXy%2BY1MPm1%2FL4GOqUBx%2F7ym%2Bx2OFo%2Bf8QclZhEtlBnlfPP6u8%2Fg%2BPsHEXWrwGZ0BTN9HTShHvbnqKGdMs2yDkzfPjb%2FxJWat%2FID68rVhJVClmRX2v5t253VZg8Ob8U5CBcSaYVBUl0j0uYcbTy7K4fmX4aa7UwIYsK9omND3lOlXmfsQfhNGZPm%2BPmgY2lrIVH90pwGINYVyNPtL0TGeaHVTr4GZXISaO2FzsPxYbMr32p&X-Amz-Signature=0f62eb248dac65f10a56abbf482ab87f6ec80d2a83bb09e9119df56fbbeed891&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU3WAEVE%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIE96vrNtd7Arp9iE%2BSXd1dgePyfSfb5A6Gl8iYAlkH%2FUAiEArZnMgFIq%2F6zY0psOvZNCXJzJR09n2h9POGrL2oH%2Bu4AqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0YhzzVekH3ZpUHRircA4iAzo3pKUUWptl0yB7jmjxptdoId7neRA2FWAbOR9H5Mz5R%2FYh6ExD5BVum%2FtkxGG4EPp%2B9RJOriEs6MYZYknXTmhoVKDnVDEqiDMAHzCBL5It4zyJY3MfPvNWcOSARNVRLSbje53E7yM6u4wZS9%2Fe4Ip%2FMnB5bQ4P6L8FgGBtchbuWwLvD1lNx0HiSb%2FgD8tZXgnTFFKaAgkUjD%2Bb%2BS4jcMMKSyqLx25LMqMDVqawRV28YviIpnaJ9p7uDn0eTrMD9nvPuxvi6oCRruVKYrOz%2F3SX2oxseg6oExprTCMuXvX0L0dzhgDujHmJp9rbaA5R90lbeqRXXp5k66oYiselPRwCRaE1iwzEeR1dFIr3SE%2B8CwFL8Ldhqtt05wZCMoXkUd4ERPBxrEfM4vAGw6rQB33ZJujhHmkLk2Vx0tG1aQ9f6fStu4zV0Lg5xYxqNIb8K3lTbQ335BUI3JKEEvcT6nzn3RQAoLBYb8%2FmfMe24FnEy3m%2B8FSnErJWxEdDaZIEA8kHdMFXgopnPrsYxxpcJdyElYv0Y5XF48D8o65yOBV%2BwC4AXO2fGfrXFuWA6REXlk4auWhLAZGwlk7k9MKEbgN8nWe5WtG54wnX%2Fx7lTKeguDZ%2BrkBUXy%2BY1MPm1%2FL4GOqUBx%2F7ym%2Bx2OFo%2Bf8QclZhEtlBnlfPP6u8%2Fg%2BPsHEXWrwGZ0BTN9HTShHvbnqKGdMs2yDkzfPjb%2FxJWat%2FID68rVhJVClmRX2v5t253VZg8Ob8U5CBcSaYVBUl0j0uYcbTy7K4fmX4aa7UwIYsK9omND3lOlXmfsQfhNGZPm%2BPmgY2lrIVH90pwGINYVyNPtL0TGeaHVTr4GZXISaO2FzsPxYbMr32p&X-Amz-Signature=df04c1cc660bcddc97ae812a580347a2e74ec2d1cc88ec814d7b00d01b428c70&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=adc43fefd171db59c3bda9928e547efda4b40a0da3a77105b0fc030ccf68fb01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=58a7f77aeea8060796b6126966d8592c6477e90f231e0f1ac03dcac93706b729&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=d230b26802d24b6816c736b900fcf294e3e8c7edf6b991c186aae34eaa574386&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=80bdd99179942ee9e600823860ceea493c658d6f47a02384fce037a032e9bbed&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=161492091b2a622667765cd1acd9d3655287b48387b04de734a9d38112d32921&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBRNYA3W%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCCyZuyah3ITEm8lMI7CfTuoj4OAFy2hSWXx%2FRGegJgBgIgMOAyvVPJNdrkOfyvNAoxlOYXL%2F2SybzIePM3E%2BzKcNoqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfQGUSTfqW%2BmZ3yFircA1%2FKdvH0z0o%2FjF1D79Jvc4cDvzZA%2FLytGEhd5SxUorMMSM6xPCaHE5x%2BGLqtQ22%2BkXLh%2FYLpqZAbB5HLzy%2Ff%2FLEWu%2BnwfdDUeob438QnozZKa6ivzzBDKaFoxc1et07FOHejYJ4N5GSTTVf6it1XClVAmHwvkUAhOM2eNZ6DqdOE5LO9r5cup67IL8uKwpLSuaabWrBZmA098ebGNo0rnVojzxvoEJe5kZN%2BrcBgE4p%2FgtlplnQrUP2MrClcfTN%2FHfPWgIn2PZKJ6RAkGjjsfNIqPLfkfEv%2BtIcW%2BmMxzBNK5ctRLtIqe3JPbswEe83VB%2Fj8ejkiUPhko9p7NuJ3W5g9nExWetfQv9S%2FZqULtZe9SP7ulSSNdD0W8gHRcN2gsBCAV2%2BpUfubPHsNhaliCNCcPzgcypKPUstzNKxy9Bzd93qdvNPnZLObBggxxU%2BWaqqVioQRRsPY8TM3x7Da75qavb78BxGuzzO4%2BLNRb5cisFtJ9mpACff8Tt6gaAUt2bctXjkT0yxrCaMTnA3h%2BX%2BxoKAEa5S9AY1khPx8z8t16mgXF5K6oYa1GJ6cUui%2FCYFL9oJx%2BvC2wS1cWJF03xHfBxnnos5bgz0St8CbxVpfHLlOkfsrDDbW5jCjMOC0%2FL4GOqUBDfjbz7UF3WoltJQ3PO3K%2FFDv41jdxghNY9XEn6B3lhmkVYocp2UzddaQUSIB44cHqdfn%2FrmEbTc62m%2F0KtY4wR9PM6RPesxdM7gJqBSAdYya%2Ftr0zNMjjuZKJn36btpbgpAfKxwrLhNI%2FhZNrM6z36jLxbSMpYtRV0XLyZoU3L0ZG4P9jjAQA6UgQxssjZVL4WlC3cwS6VGt%2FEF3D4OT1ddUkfSP&X-Amz-Signature=88da2615bfaf809bb16f34c829530d4697e1cc74d9a48ba3314eb927ef12e51b&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646THGXVS%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDO%2FrOLP%2Bx1Ne5ho2JmR0nMuT94SkVxnLreFLWTaya1%2BQIgCXzvXsrJN598hPoWegHoN1ZdDNdjSN1zqDK5pc2bfMcqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCRBgYMu8S3K2KNNLyrcAysQeRHFPwoErVYOoEaICc2V9sGAX7qMmWp7i%2B%2FE%2FAYtSpTWBvS%2BzFGpEwvXhfwDJMNdNQ3SXTxPF7ovUFqahTsNgnekSdso%2BeI2Jrtd1TIqGecvRleCgMxA%2FIwJZO%2BYQDQ1unsgccKcuhPBPGp4BA2Ood%2FhduLRpgsn0WK67nhKWfOX3weUSFkc70%2FETK44N7uuVcw1dcvKHQLPKjXm%2FPVgi4JBskUFdT0PdlRa5y3g8bcHgrS3Ze6rNaCvmti9umGlQcn6wwixAz6DIAYclBWt8xaQqIzKoBhkGyUSsObZ2nkpq1rrOrf0NLCASHx5PY5kbF05PbsT7mrg%2BwNpCYaJTAfx0QYu8PFycv1XJW3D9R9Qb%2BKOD0VBSCn3c32R9VzIrbR4%2Bfz3xJnJIwODj4AfDw9V7BRzpvwWhoXM0pKUoRoaxRpyRGquv%2BfHOX7Is%2B1pUtK6UzqLq5tCKwzvvkd2ddfsjzmO%2BKXoZiDCl7e1r7sFnSdRVRjZ895T9Ii2kjCVcUn5o6Dusjnk%2BU5na2lGhbaq13aKeqcCuZIZgHNkuHhUNL8Iwz6%2FWE9xajDnx1gDRypWsiOvCZMcohnfebQo1JCYMC0FxHXi6%2B9moeiYFgP2wiOkQAdcwcDYMOS1%2FL4GOqUByV6BUFcNJTgQZZhOSy08WNV9N8YkRvDjl43LjBl%2BEuhzZMmkxIYEs1mK7YSxqQLqbEjj2OVHy0U9qnnt59y7ZGSdXyZxJO9XOnRwkzkOlz8IlGLwZuRbaIHjyru3PBkm1QjQ390kAZZNElACA87JE8p75a5mnXafmvDG5VggRg%2Fs7ewmaueXXF%2FAvOKInu73F85BJgVvE%2FxXI4UmNI75KU%2Feqn7K&X-Amz-Signature=1152566d9970eb75aadb95e41e27d322be7c05c1138685cb4ee9388d65c70f9b&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646THGXVS%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQDO%2FrOLP%2Bx1Ne5ho2JmR0nMuT94SkVxnLreFLWTaya1%2BQIgCXzvXsrJN598hPoWegHoN1ZdDNdjSN1zqDK5pc2bfMcqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCRBgYMu8S3K2KNNLyrcAysQeRHFPwoErVYOoEaICc2V9sGAX7qMmWp7i%2B%2FE%2FAYtSpTWBvS%2BzFGpEwvXhfwDJMNdNQ3SXTxPF7ovUFqahTsNgnekSdso%2BeI2Jrtd1TIqGecvRleCgMxA%2FIwJZO%2BYQDQ1unsgccKcuhPBPGp4BA2Ood%2FhduLRpgsn0WK67nhKWfOX3weUSFkc70%2FETK44N7uuVcw1dcvKHQLPKjXm%2FPVgi4JBskUFdT0PdlRa5y3g8bcHgrS3Ze6rNaCvmti9umGlQcn6wwixAz6DIAYclBWt8xaQqIzKoBhkGyUSsObZ2nkpq1rrOrf0NLCASHx5PY5kbF05PbsT7mrg%2BwNpCYaJTAfx0QYu8PFycv1XJW3D9R9Qb%2BKOD0VBSCn3c32R9VzIrbR4%2Bfz3xJnJIwODj4AfDw9V7BRzpvwWhoXM0pKUoRoaxRpyRGquv%2BfHOX7Is%2B1pUtK6UzqLq5tCKwzvvkd2ddfsjzmO%2BKXoZiDCl7e1r7sFnSdRVRjZ895T9Ii2kjCVcUn5o6Dusjnk%2BU5na2lGhbaq13aKeqcCuZIZgHNkuHhUNL8Iwz6%2FWE9xajDnx1gDRypWsiOvCZMcohnfebQo1JCYMC0FxHXi6%2B9moeiYFgP2wiOkQAdcwcDYMOS1%2FL4GOqUByV6BUFcNJTgQZZhOSy08WNV9N8YkRvDjl43LjBl%2BEuhzZMmkxIYEs1mK7YSxqQLqbEjj2OVHy0U9qnnt59y7ZGSdXyZxJO9XOnRwkzkOlz8IlGLwZuRbaIHjyru3PBkm1QjQ390kAZZNElACA87JE8p75a5mnXafmvDG5VggRg%2Fs7ewmaueXXF%2FAvOKInu73F85BJgVvE%2FxXI4UmNI75KU%2Feqn7K&X-Amz-Signature=50b6e621a43061d3ba61eb4acbe2de2a803cf971eb782250db78cea132116195&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3OGL43S%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIHogWIfW32F%2FSyMLUt7m%2BfRMmP%2F6WJsv2r8F7QRkkJK5AiA8tDegSYS8TtPLwsXP1gNLP2E899fKZH5OmaCRqe2VcSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGLNLdWKey1z4N9ygKtwDQTcbqKqA1bFc8an1Ao%2BxeIYexKvB7T%2ByUqzD3E90MZ1Art4T5UvXPU3mlVUyI6i5SnS5LfBesnsmTb%2F1JhUQokGHE%2F6vpqyfaRum5%2BU4FmICjDlgJxmbiwgWI3wagbGB5vF0JTqwo78izwLGnBUxHh7x0SmUq%2BCQEPFmOj1%2BDRh%2FwlcEwGbmBezvtzjFksdOY6ygEmG%2FugMg%2Fvl2GKTlXqeAY74X350SC6JbG1RzEVPgftWNWfsVE1pCFVFGys7wrRlsULQDYb1EERUctyQhpq2VCYnNE4m4CkebwgVyLiGnyHSMRF%2BS8Zo1VgkmKCqImMQyRvkVp9OKVfWjd2PoGJ4gTZukODJAwOtinkeePjrngfQze1xKA15yepCYphS%2B0%2BFt5DoN3jg0mVLvxuH2WynjPjNalLZqaVeaicYWtrszQesXqQVSkTrfoqBCX9foYt0cZhG0V3UNo5aDkr8%2BxWwAGAu%2FUv2rHO%2B4voDHinRq4QNRJRF1LAgtJ4cAA2qhcadDG7QAn6Cl3b8JstsEoiUPY4peoxudRRX%2FJHjShTdCKX4lZ3bqH3y8Clm%2B88gfnPJ7aF4ju5dLTuVFNrg25ARlgCfPdN%2BThr%2FNFW3%2Bs7LvzciZYAijN%2FT6LCwwj7X8vgY6pgG13gG50uYfzOIKwIRuL9K4%2FnvpiC5Og8PJsrVsh1n4DssOVDZNUDTPlMh4cA8U%2FisJAe9XM9dOq3zTuc5Zz46Lh%2B8RPigtpmNOZN7jZn8Vl14u%2F97Ev0advyUX%2B2bD1yKfECzMPcL57c%2FeGWLAPRhT9sIYn5iNEfk7i3z%2FiMmJWhJKDlWnR3BJSwFdMLHoJpyr7m4qBwnIVNRD8WOQpcHj1pFAF4G6&X-Amz-Signature=87ab182aef8b3b5398488752e57fceadda9161c24524e0a06ea372e5f7c87c13&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5DI73IO%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIA2N8avyxfJTkR6AdTW0bNgfMD4l1rK2eKNRZv9n000IAiEAwxtyGg9PDoTujGgI5k3s8SbhB1AYxg4skqjdWUd51jsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFaPTZzUYDkDVWtymCrcA0B%2Frl%2FYHaVZZysa5zQPhrZb299hYzusOgQRtp6h2xk2fr0xmXl3UFoo2ufG6Dr3WNYezdYsrefT2FMjEJdLWweTvBFqgr2vhAcLdYNBhVZv6PfxxBYrHoaOD17U38nfCLkJT5wYpdS%2BdR%2FakwI9gLXyS0WGAqFOKBiosMKZwYq9JAXJt1E2fXnMPAZmNT7vEQkFctaCAr4P1AgNaMH9txSMmyKMvYDe%2FfMD4NwcYJajyxyJebdcgTXjJ2%2BtVDQsXDpWjc%2FwUhOmev4XlpwppO%2FpUeNQyPJmH%2Fz%2FsTy634xEGIWsYcRzK6jsk%2FIH%2B%2B28A9gydcPDZk23y0iN%2BHd7i%2BspU6B%2B%2FUWTAODZNsGFtpKVxDVjL0lsDwE5RxCe%2Fsuht9qeFZdRREJp2vS08mPdpTqcrv040uqUq3x7eklOVd%2F4ftKu3unizj0UdoN2Q9AOHPytt%2FsdGbyekFCN%2FKYTruaPOCJlrefYvW%2FGFg6pMXHmRB%2FvOtT0UjlqMxcOg0GC4Dl%2FINEetH%2BnYmtZuUbosqtySMfn6clmfXwr12FULnRZeATzMNHHrAtqwPdQGh21pgw4uOz3FMToiNPU3mD3cY4hklL5l09WvBY%2FgEl%2B3aNoGgMZZZtU4W%2FBvb64ML3K%2FL4GOqUBUfppsQ63VlPDwFQLXJjn7ReqWyyNVvh9mXdkNRlPvvqbs6XyQZbzv1VXh9Ts%2FklWsz2eRgVnHU7i7%2Futjal3WwjRgjAoasO%2FeqEx4tYc1Qze7AdT4F5a1RevHs8ZjLzepix1YDTSaPajXOvjMQdr5F1R9cJbZ90aHypfpbTtrE6VrGriHBTMOl3SQTcosNMITfUOX%2F5roONkTI0hEVeQ2bTfHP%2FU&X-Amz-Signature=66d91cd5e8257b69c80af58c4bbf9205f2f8fce9a583517ade24ad75ed3e1789&X-Amz-SignedHeaders=host&x-id=GetObject)
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