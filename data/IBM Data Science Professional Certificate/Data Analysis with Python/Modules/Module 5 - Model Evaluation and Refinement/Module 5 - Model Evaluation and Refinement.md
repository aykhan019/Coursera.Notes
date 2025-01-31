

# Module 5: Model Evaluation and Refinement
## Model Evaluation
### In-Sample vs. Out-of-Sample Evaluation
- **In-Sample Evaluation**: Measures how well the model fits the training data. It does not estimate how well the model will perform on new, unseen data.
- **Out-of-Sample Evaluation**: Assesses how the model performs on new data. This is achieved by splitting the data into training and testing sets.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/86faf38a-f355-4667-8e18-d8c7bb5daefb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=590ed6810ac156f0619c3433e4900fd1740c0dbbfd9bea9fe247c8ce96b99316&X-Amz-SignedHeaders=host&x-id=GetObject)
#### Data Splitting
1. **Training Data**: Used to build and train the model. Typically, a larger portion of the dataset.
2. **Testing Data**: Used to evaluate the model's performance. Usually, a smaller portion of the dataset, such as 30%.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/674e9221-07aa-4c6d-bf56-fc149ea7fa32/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=531f0980518441730ed339a019fa3c020f0292c64ecc8568e5189e32d5d9fbbc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/00529d67-52ea-4caa-bddd-32a758009645/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=682643b5122bb676024c906e2cd6a873fd1778cea856049dc7cb42be99df2bf1&X-Amz-SignedHeaders=host&x-id=GetObject)
3. **Splitting Data**: The dataset is divided into *k* equal parts (folds). Each fold is used once as a testing set while the remaining *k − 1* folds are used as the training set.
4. **Using **`**cross_val_score**`:
```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()
scores = cross_val_score(model, X, y, cv=3)  # 3-fold cross-validation
mean_score = np.mean(scores)
```
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2736152c-9607-455b-80f3-f9ca34029733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=e33742cb024aec849819c1963c288c1182a24df34bc131153bb68071b47e5722&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/101e6426-cc5d-43a7-90f1-de74c28d2f66/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=787658040b4ff8ced558f99068455ab065321e4178ca74e6c804eb1a0e33d63a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d0e1153e-6c20-42b7-9a45-3e20b634f29e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=7a8b6d3cddb0592f136d52a6c0161b15277418dbddff1f5a251cde1bf3479cee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Overfitting**
**Overfitting** occurs when the model is too flexible and fits the noise rather than the function:
- Example: Using a 16th order polynomial, the model does well on training data but performs poorly at estimating the function, especially where there is little training data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/2a1d0c40-83ca-453f-9e43-16e3448b7782/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=803b9aaa99f74183d84e887a1a3534c9217195a4dba7b635de7175072602f3ee&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Optimal Polynomial Order**
- To determine the best order, we use the mean square error (MSE) for training and testing sets.
- The best order minimizes the test error.
- Errors on the left indicate underfitting, while errors on the right indicate overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/fd80c852-c3fe-4216-92e4-f98d900c76b1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=ce633a09c787b841a4ec5b7e101fa1f4f9169d9c0782f8fa9356f1b08ec15d4f&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Irreducible Error**
- Noise in the data contributes to the error, which is unpredictable and cannot be reduced.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d8a9198-e0ee-4810-9b48-3c77c2a9497f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=6ec75ca6844e7d2e6d28f097d001de641d5bf5b985cbe0ec34a9b61d6c5a1361&X-Amz-SignedHeaders=host&x-id=GetObject)
### **Example with Real Data**
- When using horsepower data:
	- A linear function fits the data better than just using the mean.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/865a8b17-616f-4900-992b-795b570f91a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H62NYXM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaS9LaoMA2%2B%2FV76esAiOxjiUOI%2BXoGaxVnRAaEeMniGQIhALMutNOGDsGJqp%2FJecmSPsswsd%2F063iI7Vk5A3nWynWOKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC%2B6GdewaFsuBlQboq3AOezoJqHyCy4Ezq0Fuhm76N%2BTnsD5YeBfM8P26CRypaNXvpVZT%2BSy5LwxVZpkiDYVgKfQV2gItBYv%2BVbph1cqWx%2BqlNXmayjfZCD9%2FhAG%2B3WD0PNj8cIxr4pGnHwmg2y1Ubsh8AQbQAONQPqoWQw9yNW6BCC8%2FmtUeCRTbHHNTcFuWjXgas%2F90cDFkxYCGAGNpUAFQJV0yRrO2hNWET2gGNpOS9qSjinOjIMBfjYvnXE%2FI3O8M%2Bfuvbgz%2Bs%2FA3Vl5vQjwOq0u27%2FJgHswsfgcB67NarEABw9ZZthRE00dijcjrnQlN7vJT0g2775kn6Fdk7O%2BDKgZEjycMJDl0JnyzYX6i8WYW4lynffJKX9alWA184pUX8QV2fv3nFHVyWvlyQ6Z7t%2FSGcOAjpTqC6eUlrnWCJjVfjPUGewtULDNMr5elPtR0er7ZPTgYLR61ib0AB8bluZCculrrY4b3uMiHEj%2FKTzezyA5QmgYjlGQshicMatNXiSM%2FyZ5OKKkL04Bn%2Fvy4%2FZQtkw7kFgyhcE3y9OJ6BHHXvBirq%2BQKI7fuo9uhw2JGPC%2FBxgmcdrKxfnwCrHD6TmIMWB7ZKfpOFq5GMxfXnHwgYjbuPobEPZ86Lj0201UUxLgEUwWK0hTD8rPO8BjqkAWx54YpWNP89m%2BWYLnBZG91gT4Zy%2BF8QTY1NhJjZBiXbN7Osnv0rFY%2FlAM67mMOLbld8yTWZ1ReOYzaHBY8nWFJJwNdDZfxuezpClp0w8oGH%2FiI1hGKkgeECMknqKR2L5gP2Z8w338%2BXo9QMn%2Fq2msSrrRcL2K9x4PgdKVHF53%2FDzeygJQZjyxlxAbE5DnrlUmK%2BOfqHwTDKOJmGRFrEK6rb5ZnX&X-Amz-Signature=64697a05db802607226ab14839f492c01c285a34f2074ff660f568b1d4f95515&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A second and third order polynomial improve the fit.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c2d83fc-759c-450f-8281-3eb119ec3a85/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H62NYXM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaS9LaoMA2%2B%2FV76esAiOxjiUOI%2BXoGaxVnRAaEeMniGQIhALMutNOGDsGJqp%2FJecmSPsswsd%2F063iI7Vk5A3nWynWOKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC%2B6GdewaFsuBlQboq3AOezoJqHyCy4Ezq0Fuhm76N%2BTnsD5YeBfM8P26CRypaNXvpVZT%2BSy5LwxVZpkiDYVgKfQV2gItBYv%2BVbph1cqWx%2BqlNXmayjfZCD9%2FhAG%2B3WD0PNj8cIxr4pGnHwmg2y1Ubsh8AQbQAONQPqoWQw9yNW6BCC8%2FmtUeCRTbHHNTcFuWjXgas%2F90cDFkxYCGAGNpUAFQJV0yRrO2hNWET2gGNpOS9qSjinOjIMBfjYvnXE%2FI3O8M%2Bfuvbgz%2Bs%2FA3Vl5vQjwOq0u27%2FJgHswsfgcB67NarEABw9ZZthRE00dijcjrnQlN7vJT0g2775kn6Fdk7O%2BDKgZEjycMJDl0JnyzYX6i8WYW4lynffJKX9alWA184pUX8QV2fv3nFHVyWvlyQ6Z7t%2FSGcOAjpTqC6eUlrnWCJjVfjPUGewtULDNMr5elPtR0er7ZPTgYLR61ib0AB8bluZCculrrY4b3uMiHEj%2FKTzezyA5QmgYjlGQshicMatNXiSM%2FyZ5OKKkL04Bn%2Fvy4%2FZQtkw7kFgyhcE3y9OJ6BHHXvBirq%2BQKI7fuo9uhw2JGPC%2FBxgmcdrKxfnwCrHD6TmIMWB7ZKfpOFq5GMxfXnHwgYjbuPobEPZ86Lj0201UUxLgEUwWK0hTD8rPO8BjqkAWx54YpWNP89m%2BWYLnBZG91gT4Zy%2BF8QTY1NhJjZBiXbN7Osnv0rFY%2FlAM67mMOLbld8yTWZ1ReOYzaHBY8nWFJJwNdDZfxuezpClp0w8oGH%2FiI1hGKkgeECMknqKR2L5gP2Z8w338%2BXo9QMn%2Fq2msSrrRcL2K9x4PgdKVHF53%2FDzeygJQZjyxlxAbE5DnrlUmK%2BOfqHwTDKOJmGRFrEK6rb5ZnX&X-Amz-Signature=4d9ed3557a08dec9bb58430377bd01c4b34b5be98e2633c4c5072e300615e707&X-Amz-SignedHeaders=host&x-id=GetObject)
	- A fourth order polynomial shows erroneous behavior.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/a041aae4-06b4-4cd0-8ec4-4caa50fd1ca7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H62NYXM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaS9LaoMA2%2B%2FV76esAiOxjiUOI%2BXoGaxVnRAaEeMniGQIhALMutNOGDsGJqp%2FJecmSPsswsd%2F063iI7Vk5A3nWynWOKogECL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxC%2B6GdewaFsuBlQboq3AOezoJqHyCy4Ezq0Fuhm76N%2BTnsD5YeBfM8P26CRypaNXvpVZT%2BSy5LwxVZpkiDYVgKfQV2gItBYv%2BVbph1cqWx%2BqlNXmayjfZCD9%2FhAG%2B3WD0PNj8cIxr4pGnHwmg2y1Ubsh8AQbQAONQPqoWQw9yNW6BCC8%2FmtUeCRTbHHNTcFuWjXgas%2F90cDFkxYCGAGNpUAFQJV0yRrO2hNWET2gGNpOS9qSjinOjIMBfjYvnXE%2FI3O8M%2Bfuvbgz%2Bs%2FA3Vl5vQjwOq0u27%2FJgHswsfgcB67NarEABw9ZZthRE00dijcjrnQlN7vJT0g2775kn6Fdk7O%2BDKgZEjycMJDl0JnyzYX6i8WYW4lynffJKX9alWA184pUX8QV2fv3nFHVyWvlyQ6Z7t%2FSGcOAjpTqC6eUlrnWCJjVfjPUGewtULDNMr5elPtR0er7ZPTgYLR61ib0AB8bluZCculrrY4b3uMiHEj%2FKTzezyA5QmgYjlGQshicMatNXiSM%2FyZ5OKKkL04Bn%2Fvy4%2FZQtkw7kFgyhcE3y9OJ6BHHXvBirq%2BQKI7fuo9uhw2JGPC%2FBxgmcdrKxfnwCrHD6TmIMWB7ZKfpOFq5GMxfXnHwgYjbuPobEPZ86Lj0201UUxLgEUwWK0hTD8rPO8BjqkAWx54YpWNP89m%2BWYLnBZG91gT4Zy%2BF8QTY1NhJjZBiXbN7Osnv0rFY%2FlAM67mMOLbld8yTWZ1ReOYzaHBY8nWFJJwNdDZfxuezpClp0w8oGH%2FiI1hGKkgeECMknqKR2L5gP2Z8w338%2BXo9QMn%2Fq2msSrrRcL2K9x4PgdKVHF53%2FDzeygJQZjyxlxAbE5DnrlUmK%2BOfqHwTDKOJmGRFrEK6rb5ZnX&X-Amz-Signature=cfd0f286a2b8a7029e0adab241504bcafd3737bbb27c816ae6706f5eee5bbf15&X-Amz-SignedHeaders=host&x-id=GetObject)
### **R-squared Analysis**
- Plot the R^2 value against the order of polynomial models.
- The optimal order has an R^2 close to one.
- A drastic decrease in R^2 beyond the optimal order indicates overfitting.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/92ce658f-7383-4bb3-91c3-e26437b3c5e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=ee87163991120c386f9c76818257f6f154d027f3fe91e68cc25b1d57c3876ba6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c53c7de-8745-4d43-89cc-fa5f491fbfe5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=3e213c9625a7cc8fe27d5d1998333997a2594501746c6cfd7eb1f4dafb4fcdaf&X-Amz-SignedHeaders=host&x-id=GetObject)
This process helps in identifying the best polynomial order that minimizes the generalization error and avoids underfitting or overfitting.
___
## **Introduction to Ridge Regression**
For models with multiple independent features and ones with polynomial feature extrapolation, it is common to have colinear combinations of features. Left unchecked, this multicollinearity of features can lead the model to overfit the training data. To control this, the feature sets are typically regularized using hyperparameters.
Ridge regression is the process of regularizing the feature set using the hyperparameter alpha Ridge regression can be utilized to regularize and reduce standard errors and avoid over-fitting while using a regression model.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c39a38d-2d49-4041-bd79-3aca0139bfb3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=25434f8ef3acda541c2a8ed687c315b1aa3ff6624e1d950d63deb6f944bedfb5&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d6cfad56-e517-4b28-9645-3de06413a2b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=048ead3e80671d129aaf8e33b2116b84f56ae11ac88aae7040eb907743856139&X-Amz-SignedHeaders=host&x-id=GetObject)
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4e4309f5-805f-43a0-8547-9e8781fd1ca4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=95cba27958e662bc5e09311b16fcffe5827d8dba5dbd9abe93556d7ca8c7a8df&X-Amz-SignedHeaders=host&x-id=GetObject)
### Ridge Regression
**Overview**: Ridge regression is a technique used to prevent overfitting in polynomial regression by controlling the magnitude of polynomial coefficients.
### Key Concepts
10. **Overfitting**:
	- **Problem**: Higher-order polynomials can fit training data very well, but might overfit, especially in the presence of outliers or noisy data.
	- **Example**: A 10th-order polynomial fitting data with an outlier may produce large coefficients, which can misrepresent the true function.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/3781e151-64db-4738-9f89-94f9f9c0c096/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EZCAK3A%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZjeZRoBHmsOvkveY%2Bf2KqJPWSp8ej4nhpMaisoWXRbAiAM7dBhQKeTDJGbFBKmz6jKAx0l3XrQvXW404r6Sp3LeSqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUTiyTrDl2%2FmIrjWYKtwDQ2ZQ%2F7xnUBh6TffSza4J3HxTKweiKXot621JqUBxW9qs5nSKDHStzqMDkusOVP5FRm9MwCatejROu8yl6cwchSdJfKwN%2FDk1YQ3JxCxvjEB1EttpLh9GdfhZqOoQ83E0Wbma5Em5K3EGnIphQhL5pOw%2FIJWJBzZ4RDYXMbWveugJVvqpdu0IBn7KSZ5bkftJ20W%2FY85UQWqcT93vhy%2BX1qOzMtQv29fLk6x56l%2FbZaKdxZKslkdcxLccSaUofMnsea3PvkSXQGAFPs80hbUfagTu0V6%2FaGMFRipNuYSCdjHfZr3jIsqKjDOkSo6vAL%2F8CgfQb1jpRWDRv%2B8klmVIuYRmbX8VX0IpwDuCwut%2FGk6yh95V1zKw4adR%2FaGwtc4LyX%2FCwaOkACh%2BJeswGtphWOHmZsgQTgqFJ76Yd3uVCL0RT4SZKt5JIqi2p47IU28MLEYt%2B%2FofeYyTl1chWZ0JMVZupGowtACzNwVu6IbuNiPEU8PeRjjY9ASeXE0XpZOy%2B186BmNVLKAouA4kNz3kWpchJ4rTn9NcxaAjyhuXF9slF%2BUx6K7nfUhYxA0gzgcxShoPQTNxBoaKZD0PbexSBOYOm7wkZgtYhmZY11FBprsDnjq1c9JaeGwrZwsw%2BazzvAY6pgHgYo55HoNLT%2B01c%2FQFzLXH0d9bJOGqa3lsOYO%2BOfvbeCMI86O94WLXSy%2B1ohyODqdvdGx1PDnCm%2Fl2YTwmdV%2Bx7U%2F%2FnHaQ%2BNqIfSkY7tMIHYDQNhVpa2QS4YlFa5NTb8qXUGUBrrgec9%2Fz7o50Rt5bzP6sMV33dD4akBztZq2mxexPCiD7mwZycJAfWNgYrRm3NTM29139i2J4am%2FrAsNr0q8Ldrz9&X-Amz-Signature=2292944beafd3b7adf6f5072d39e5b3f70328ed7ada8acfb7b1e825fbdf745b7&X-Amz-SignedHeaders=host&x-id=GetObject)
11. **Ridge Regression**:
	- **Purpose**: Ridge regression addresses overfitting by introducing a parameter, Alpha ($ \alpha $), which penalizes large coefficients.
	- **Effect**: As Alpha increases, the magnitude of the coefficients decreases, which can prevent overfitting.
	- **Alpha Selection**:
		- **Too Small Alpha**: Might still overfit the data.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/af571e3b-ec69-47c8-b4ce-679c07c22950/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZZYDP6S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWfNzWMphgUubwQaOaZNxGXhjEnwsKNB2aL4EJXRzoNAiBfqkVeUxbuMj6ubnA0lKtLeo3PRitg%2BBYkptQKCuakyCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgg%2B71EDxyIyr%2F6ITKtwDbDurjngsSwNUQO4wlaSa3B5l8wqRe0h%2ByHYAr3O9b1ewBYOeHwKT0F3JUgfUohI3MfFRJw63Ifbdy2xfQg%2FGstJK8uduixVS6%2FN5vNB55LQK6K2nVoIbhQdSX0Uwl4xVg%2B8u9QLXKOzOxbUiBUOwF4SDgyCk7ZljoYMx9%2FNkutjL8TaKRv5xle6bYr2gGrSHjYuXWr2G0ymtHYFz6R5ph0dZQY8dxwCTFv%2FIi2leoOJ8%2BDpwFyAb8j0HCw%2FDF2oQU1FFVBIJoKJDcKT7IISeFzR%2BhwhDg0bWvCwX4l3D1Ts%2Fh1%2BmYBEmR40bRGk8ZQVxFh2i9QvH%2F8y5d%2Blw3MaoWrXucvAn9jjFj2%2BQC%2FYSoBgbVc0wjA%2Blankf2f9%2B%2F3EGS4AbLaW3V3CWgMsHE%2FHrGlw3rQDU1WZR7Zd7jpg%2BiOXL0LWqqQscG53DaZQ1JXexJAIpfHOqnK8uPbbLzJo2s74WdSHe5J8MKSi0yMLFCyAQ5ATO6vrR3VtU6vDqj2zk5iHXbSQO8xqdhejpIroG0C833YFeFmIQYryvi8mYa0kGjDrMSKiL3yWIasg4QdHAjSIPIGR%2BtPHRMwYJ079eVSIu%2F0xGQtc9V16bawnd0lRRWP%2FSq2CvS%2BVsYyowzazzvAY6pgGD%2BwxWQB8U5zyBtswvXBSS%2FLltQsj3TNzL3cGoleZd24KV5TrqpeAluQ%2BOh9Ux9OPd%2B8X3JN2Rw3Ji7si2JMpZgbrr5zrD3rPlXV6OcL8VVZ6cLiP2mebycTOecBLgrsDKBcamnZZkGSZcyGIiIqkg%2B93%2FsUAVkY15vbksFRZXa6QFmptRkN5DJrKTIGZUDT3kqY99yp8YZLcUt11SovXfjmyms4an&X-Amz-Signature=2d667d7db090186c1307957ee012835e8bdc29cdb2844f80a4c130dbdba65c9e&X-Amz-SignedHeaders=host&x-id=GetObject)
		- **Too Large Alpha**: Can lead to underfitting as the model becomes too simple.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/e39a5304-aac2-4d02-a4a2-dc0986a76649/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZZYDP6S%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWfNzWMphgUubwQaOaZNxGXhjEnwsKNB2aL4EJXRzoNAiBfqkVeUxbuMj6ubnA0lKtLeo3PRitg%2BBYkptQKCuakyCqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgg%2B71EDxyIyr%2F6ITKtwDbDurjngsSwNUQO4wlaSa3B5l8wqRe0h%2ByHYAr3O9b1ewBYOeHwKT0F3JUgfUohI3MfFRJw63Ifbdy2xfQg%2FGstJK8uduixVS6%2FN5vNB55LQK6K2nVoIbhQdSX0Uwl4xVg%2B8u9QLXKOzOxbUiBUOwF4SDgyCk7ZljoYMx9%2FNkutjL8TaKRv5xle6bYr2gGrSHjYuXWr2G0ymtHYFz6R5ph0dZQY8dxwCTFv%2FIi2leoOJ8%2BDpwFyAb8j0HCw%2FDF2oQU1FFVBIJoKJDcKT7IISeFzR%2BhwhDg0bWvCwX4l3D1Ts%2Fh1%2BmYBEmR40bRGk8ZQVxFh2i9QvH%2F8y5d%2Blw3MaoWrXucvAn9jjFj2%2BQC%2FYSoBgbVc0wjA%2Blankf2f9%2B%2F3EGS4AbLaW3V3CWgMsHE%2FHrGlw3rQDU1WZR7Zd7jpg%2BiOXL0LWqqQscG53DaZQ1JXexJAIpfHOqnK8uPbbLzJo2s74WdSHe5J8MKSi0yMLFCyAQ5ATO6vrR3VtU6vDqj2zk5iHXbSQO8xqdhejpIroG0C833YFeFmIQYryvi8mYa0kGjDrMSKiL3yWIasg4QdHAjSIPIGR%2BtPHRMwYJ079eVSIu%2F0xGQtc9V16bawnd0lRRWP%2FSq2CvS%2BVsYyowzazzvAY6pgGD%2BwxWQB8U5zyBtswvXBSS%2FLltQsj3TNzL3cGoleZd24KV5TrqpeAluQ%2BOh9Ux9OPd%2B8X3JN2Rw3Ji7si2JMpZgbrr5zrD3rPlXV6OcL8VVZ6cLiP2mebycTOecBLgrsDKBcamnZZkGSZcyGIiIqkg%2B93%2FsUAVkY15vbksFRZXa6QFmptRkN5DJrKTIGZUDT3kqY99yp8YZLcUt11SovXfjmyms4an&X-Amz-Signature=7d7188d7048bbab95c24a3d8b8ce62feb260fb9b58dd5bb55b61df41912be775&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/4d3f8068-85d5-4c62-bc0e-0eaf7b277985/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5FLKP2Z%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEOKaoUNx1pcvX%2BN6Q0bsUXsjp2LmNEMw0FXGmt128GXAiBKWNcKXlMeOIoJ%2BgqGHw3P0EUTCkyk6RFwg%2FXiwfFl2SqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiRuNay4AS2kcpjg9KtwDch9sGjruukph6o%2BEWyEf1Xo5atoRRiRRzvhyFjh24IwSHBsw1GCk61tm4aR5F5Aqwk4hoV7HQ5cn5Eg6vymmMyjtIk8UQLLYmm7aQ3XGbYt6Vtj3M0dClHvSVHKJ7w4UQTWzYj5vn0OQnRtvz5mtx6wRIOPMwNt6voUvmgud%2FpEP7U7Ybo%2Fp0Dht1LfOZ0CIs%2FMK0%2BOIrEaiSjBkuri6OPHwNTAd6qHnlri4AfdnGjkbQK8HeJ3QBozj4Ea3zKH4YcP4HC7oSZn90878MtIg6f6dsa2OfCFIlpHeuOz2IXChZIaMkI2wdhuQeXbqsOaI7yTeju%2BRJZrBlE6YEPpFiAu%2FW01VWcCzJpJL5qwy2FQmrkHyB1S8sVTjPhnWKbV246MEfO1OVyDu5odseY3tDaHGyCXsS7Wjz%2BCik7%2FutmAPz2SB%2Bx7K4n4t4UTk9hq%2BB9tyvEqo124WnuyycN78iQj8CT%2BlbIk5GXndtQuaKigH183gzMxr2hnCZs5nsIuc51wivXIUbROioWUbnd45q0c5L7hWE1rQzOd5BDYRwp3gSan6j32aT8I0Nx1p8PWgnwXVooiZbzM4%2BnCG0mC%2F4rM38U9Ux1DPTTTFjBHFeO4Iky31ksZhGxQwasQwsKzzvAY6pgGX3NOrSzt49Y9oXgB%2F48AbADvP5FX45TF%2BZIDrBsx75gxVxLvj5l48wvucbTnVxmSY8i7u5Xdwpq80wOYUi00py6n2bDD%2B0c8gsR7sXSAM9tXD5Wgsirl%2F3nbHt%2Bqi0qA3TWOlmNI6XXgMn15JgSgElZ4IGXjl9ip%2Fc5OoFen%2FQgwFT4ZmeXdqNUDdemPz4eGSP%2B2hSuKUnCM%2F6HiSDtgpdBnYGt3Z&X-Amz-Signature=70071d226f0e0d640df0e731ff7be5f6a8384dc9608708785904f462d66dc5c1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/93fb6806-f698-492b-93cc-a2658013d88d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDOF7B4U%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T141308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICkjVXfMJWthEsuWa7FX7PebRmELRlFv9R7X61FVZkJVAiB9FYMvd%2BSzr43L5aWiCDr%2BiD5xJL2ciYRyPIj0iR5WBiqIBAi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDSviHdRIVqdvVYKxKtwDVNJ6%2BoaqU2jpnnCGFeFnqVdBiOukqRbAPBAZULNDtf3Ybrpc3Py24vNNkPKUgYWIBF0B%2BN%2FwxM235YfoNlrcQCGwMD4LFpAl6zwTTFWkDsajvhEdEknRMqzVstguOXiAUpwIpi8mAx%2FzRyg3u4tpx%2FvrpfkPKocRnIKg3rOdmUzKtibl7l0GfbrJE4QKIK3fMdQ1nRpFl%2F9v0Ar5CdCikv%2BlGXZINzPkPyWPrl2aufHykEyVjSOs%2F4unBNiGuoBtaS9LqOTvvrFZyZrkWs6f5%2F4oa48mrnd0pa7Z1rP0%2BA55rsHjduPcOFjugthxTz%2FKt%2B%2BFvQKf09A2Pp0RBDBRRfguLAaiE0GH7HMlIP8qvS%2B1Y6mtk0Em%2B5yvqWBxCzwn6qZEB%2BNvMnsX8y3bf4CUvJsipRYgSFSPfRW%2BsYMAfn9D4kOGjrzo8Ei%2B4RFX1jG55VhSRfxZmRtXv28vpUaHWrGZzCKr7otP10qenhcUuXZeLC77FLLFN5d7xLOEsc0NZNlG%2FWdHzcxQzueeqt4AeBS5eLZck3yz0uHOHrF1afmzFHO8LDoLLBPyafI8isry8NqH5XA4auvS36T8CZgJNoEzMVk5xPML%2FpLxkuofgVg5GK03TB9OyJ9%2FVfYw5KzzvAY6pgGMAfTYqL7Zwng98QOiR9QJKZUlSFLGXbVUu8wlXLX9JXapSlY7qbriQqeU%2BLgUs7n1eXrMu3i1rM4EazCcIIKwjFY8%2ByXpzqQKmnrJywNCirQoqcjUa1UJxE5AkkyOemZErrpheX2AWwsL7H2YiQU8cyQ6TiWscgnpHEFx6bLYE8FezJJZ8jxlpoCd3%2FWiUMcJhY1KCNBYjIoLh3%2BzcpE2IlU0OE3B&X-Amz-Signature=c430e4b69f1a0d53ccfb5a2434a6acbada5726f79f67137aedb1005c0031927e&X-Amz-SignedHeaders=host&x-id=GetObject)
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